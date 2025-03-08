import cv2
import os
import utils.file_utils as fu
import utils.directory_links as dl

# Diretório de saída
OUTPUT_DIRECTORY = 'results/tests/3_deteccao_de_contornos/contornos'

for path in dl.DIRECTORY_TEST_IMAGES_LINKS:
    
    if not os.path.exists(path):
        print(f"Erro: Arquivo não encontrado - {path}")
        continue
    
    image = cv2.imread(path)
    if image is None:
        print(f"Erro: Não foi possível carregar a imagem - {path}")
        continue
    
    # Converte para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecta contornos
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Desenha os contornos na imagem
    output = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    filename = fu.get_unique_filename(OUTPUT_DIRECTORY, "contornos.jpg")
    save_path = os.path.join(OUTPUT_DIRECTORY, filename)
    cv2.imwrite(save_path, output)
    
    print(f'Contornos detectados e salvos em {save_path}')