import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

def showMultipleImageGrid(imagesArray):
    """
    Exibe uma grade de imagens de forma adaptativa, com base na quantidade de imagens.

    Parâmetros:
        imagesArray (list): Lista de imagens (arrays NumPy).
        titlesArray (list ou str): Lista de títulos para as imagens ou um título único.
    """
    num_images = len(imagesArray)
    
    # Se não houver imagens, retorne
    if num_images == 0:
        print("ERRO: A lista de imagens está vazia!")
        return

    # Calcula o número de linhas e colunas para a grade
    if num_images == 1:
        x, y = 1, 1
    else:
        # Tenta criar uma grade o mais quadrada possível
        y = int(np.ceil(np.sqrt(num_images)))  # Número de linhas
        x = int(np.ceil(num_images / y))       # Número de colunas

    # Cria a grade de subplots
    fig, axes = plt.subplots(y, x, figsize=(x * 4, y * 4))  # Ajuste o tamanho da figura conforme necessário

    # Se houver apenas uma imagem, exibe diretamente
    if num_images == 1:
        imgMPLIB = cv2.cvtColor(imagesArray[0], cv2.COLOR_BGR2RGB)
        axes.imshow(imgMPLIB)
        axes.set_title(imagesArray[0])
        axes.axis('off')
    else:
        # Preenche a grade com as imagens
        for i, img in enumerate(imagesArray):
            # Escolhe o eixo correto dependendo da dimensionalidade de `axes`
            if y == 1:
                ax = axes[i % x]  # Caso 1 linha
            elif x == 1:
                ax = axes[i]  # Caso 1 coluna
            else:
                ax = axes[i // x, i % x]  # Caso geral (mais de uma linha e coluna)

            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ax.imshow(imgMPLIB)
            # TODO: Tentar colocar nome da imagem depois
            # ax.set_title(imagesArray[i])
            ax.axis('off')

        # Remove eixos vazios se houver mais células do que imagens
        for i in range(num_images, x * y):
            if y == 1:
                ax = axes[i % x]  # Caso 1 linha
            elif x == 1:
                ax = axes[i]  # Caso 1 coluna
            else:
                ax = axes[i // x, i % x]  # Caso geral (mais de uma linha e coluna)
            ax.axis('off')

    fig.tight_layout(pad=1.0)  # Ajusta o espaçamento entre as imagens
    plt.show()
    
def showImage(img, title=None):
    """
    Exibe uma única imagem em uma janela.

    Parâmetros:
        img (numpy.ndarray): A imagem a ser exibida (em formato BGR ou RGB).
        title (str, opcional): Título da imagem. Se None, nenhum título será exibido.
    """
    # Converte a imagem para RGB se estiver em BGR
    if len(img.shape) == 3 and img.shape[2] == 3:  # Verifica se a imagem é colorida (3 canais)
        imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else:
        imgMPLIB = img  # Se a imagem já estiver em RGB ou for em escala de cinza

    # Exibe a imagem
    plt.imshow(imgMPLIB)
    if title:
        plt.title(title)
    plt.axis('off')  # Remove os eixos
    plt.show()

def showImageGrid(image, title=None):
    """
    Exibe uma imagem em uma grade (subplot) com um título.

    Parâmetros:
        image (numpy.ndarray): A imagem a ser exibida (em formato BGR ou RGB).
        title (str, opcional): Título da imagem. Se None, nenhum título será exibido.
    """
    # Converte a imagem para RGB se estiver em BGR
    if len(image.shape) == 3 and image.shape[2] == 3:  # Verifica se a imagem é colorida (3 canais)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Cria a figura e o eixo
    fig, axis = plt.subplots()
    
    # Exibe a imagem
    axis.imshow(image)
    if title:
        axis.set_title(title)
    axis.axis('off')  # Remove os eixos
    plt.show()
    
def get_unique_filename(base_path, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(base_path, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1

    return new_filename