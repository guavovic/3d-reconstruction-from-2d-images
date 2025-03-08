import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import utils.file_utils as fu
import utils.pyplot_utils as ppu
import utils.directory_links as dl

def remover_fundo(image_path, output_dir, blur=21, canny_thresh_1=10, canny_thresh_2=200, mask_dilate_iter=10, mask_erode_iter=10):
    """
    Remove o fundo de uma imagem e salva o resultado com fundo transparente.

    Parâmetros:
        image_path (str): Caminho da imagem de entrada.
        output_dir (str): Diretório de saída para salvar a imagem processada.
        blur (int): Tamanho do kernel para o desfoque Gaussiano.
        canny_thresh_1 (int): Limiar inferior para o detector de bordas Canny.
        canny_thresh_2 (int): Limiar superior para o detector de bordas Canny.
        mask_dilate_iter (int): Número de iterações para dilatar a máscara.
        mask_erode_iter (int): Número de iterações para erodir a máscara.

    Retorna:
        str: Caminho da imagem salva.
    """
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {image_path}")

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    # Converte para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecta bordas
    edges = cv2.Canny(gray, canny_thresh_1, canny_thresh_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    # Encontra contornos
    contour_info = []
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        contour_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c)))

    # Ordena os contornos por área (do maior para o menor)
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)

    if not contour_info:
        raise ValueError("Nenhum contorno válido encontrado na imagem.")

    # Pega o maior contorno
    max_contour = contour_info[0][0]

    # Cria uma máscara preta
    mask = np.zeros_like(gray)

    # Desenha o maior contorno na máscara (preenchido de branco)
    cv2.fillConvexPoly(mask, max_contour, 255)

    # Suaviza a máscara
    mask = cv2.dilate(mask, None, iterations=mask_dilate_iter)
    mask = cv2.erode(mask, None, iterations=mask_erode_iter)
    mask = cv2.GaussianBlur(mask, (blur, blur), 0)
   
    # Cria uma imagem com fundo transparente
    bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    bgra[:, :, 3] = mask # Define o canal alpha com base na máscara

    filename = fu.get_unique_filename(output_dir, 'rembg.png')
    save_path = os.path.join(output_dir, filename)
    cv2.imwrite(save_path, bgra)

    return save_path

def remover_fundo_grabcut(image_path, output_dir):
    """
    Remove o fundo de uma imagem usando o algoritmo GrabCut.

    Parâmetros:
        image_path (str): Caminho da imagem de entrada.
        output_dir (str): Diretório de saída para salvar a imagem processada.

    Retorna:
        str: Caminho da imagem salva.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {image_path}")

    # Carrega a imagem
    original_image = cv2.imread(image_path)
    
    if original_image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)

    binarized_image = cv2.adaptiveThreshold(
        gray_image,
        maxValue=1,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY,
        blockSize=9,
        C=7,
    )

    # Cria uma máscara inicial (tudo é considerado fundo)
    mask = np.zeros(original_image.shape[:2], np.uint8)
    mask[:] = cv2.GC_PR_BGD
    mask[binarized_image == 0] = cv2.GC_FGD

    # Aplica o GrabCut
    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64) 
    # Define boundary rectangle containing the foreground object
    height, width, _ = original_image.shape
    left_margin_proportion = 0.3
    right_margin_proportion = 0.3
    up_margin_proportion = 0.1
    down_margin_proportion = 0.1

    boundary_rectangle = (
        int(width * left_margin_proportion),
        int(height * up_margin_proportion),
        int(width * (1 - right_margin_proportion)),
        int(height * (1 - down_margin_proportion)),
    )
    
    number_of_iterations = 5
    
    cv2.grabCut(
        original_image,
        mask,
        boundary_rectangle,
        background_model,
        foreground_model,
        number_of_iterations,
        cv2.GC_INIT_WITH_MASK,
    )

    # Cria uma máscara binária (0 = fundo, 1 = primeiro plano)
    grabcut_mask = np.where((mask == cv2.GC_PR_BGD) | (mask == cv2.GC_BGD), 0, 1).astype("uint8")

    # Cria uma imagem com fundo transparente
    bgra = cv2.cvtColor(original_image, cv2.COLOR_BGR2BGRA)
    bgra[:, :, 3] = grabcut_mask * 255  # Define o canal alpha com base na máscara

    filename = fu.get_unique_filename(output_dir, 'rembg_grabcut.png')
    save_path = os.path.join(output_dir, filename)
    cv2.imwrite(save_path, bgra)

    return save_path

def main():    
    OUTPUT_DIRECTORY = 'results/tests/2_deteccao_de_contornos/remocao_de_fundo'
    edited_images = []

    for path in dl.DIRECTORY_TEST_IMAGES_LINKS:
            saved_path = remover_fundo_grabcut(path, OUTPUT_DIRECTORY)
            print(f'Imagem processada e salva em {saved_path}')
            current_image = cv2.imread(saved_path, cv2.IMREAD_UNCHANGED)
            edited_images.append(current_image)
            
    # print(f"Total de imagens processadas: {len(editedImages)}")
    
    ppu.showMultipleImageGrid(edited_images)

if __name__ == "__main__":
    main()