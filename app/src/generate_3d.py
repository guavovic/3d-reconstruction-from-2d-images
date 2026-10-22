import time
from PIL import Image
import numpy as np
import rembg
import torch
from torchvision.transforms import Compose, Resize, ToTensor, Normalize
import cv2
import os
from src.config import CACHE_PATH
from src.utils import log_message

os.makedirs(CACHE_PATH, exist_ok=True)

def generate_3d_model(image):
    """
    Gera um modelo 3D a partir de uma imagem 2D.
    """
    log_message("Tratando a imagem...")
    image = preprocess_image(image)
    time.sleep(20)  # Pausa de 20 segundos
    
    log_message("Removendo o fundo da imagem...")
    image = remove_background(image)
    time.sleep(20)  # Pausa de 20 segundos
    
    log_message("Gerando mapa de profundidade...")
    depth_map = generate_depth_map(image)
    time.sleep(20)  # Pausa de 20 segundos

    log_message("Convertendo mapa de profundidade em modelo 3D...")
    obj_model = depth_map_to_obj(depth_map)
    
    return obj_model

def preprocess_image(image):
    """
    Realiza o pré-processamento da imagem (redimensionamento, normalização, etc.).
    """
    image = image.resize((256, 256))
    image_array = np.array(image)
    image_array = image_array / 255.0
    
    # Salva a imagem pré-processada no cache
    save_to_cache(image_array, "preprocessed_image.png")
    
    return image_array

def remove_background(image):
    """
    Remove o fundo da imagem usando a biblioteca rembg.
    """
    image = Image.fromarray((image * 255).astype(np.uint8))
    output = rembg.remove(image)
    output_array = np.array(output)
    
    # Salva a imagem sem fundo no cache
    save_to_cache(output_array, "no_background_image.png")
    
    return output_array

def generate_depth_map(image):
    """
    Gera um mapa de profundidade a partir da imagem usando o modelo MiDaS.
    """
    # Carrega o modelo MiDaS
    model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
    model.eval()
    
    # Pré-processamento da imagem para o modelo MiDaS
    transform = Compose([
        Resize((384, 384)),  # Redimensiona para o tamanho esperado pelo modelo
        ToTensor(),  # Converte para tensor
        Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normaliza
    ])
    
    # Aplica o pré-processamento
    input_image = transform(image).unsqueeze(0)
    
    # Gera o mapa de profundidade
    with torch.no_grad():
        depth_map = model(input_image)
    
    # Converte o mapa de profundidade para um array numpy
    depth_map = depth_map.squeeze().cpu().numpy()
    
    # Salva o mapa de profundidade no cache
    save_to_cache(depth_map, "depth_map.png")
    
    return depth_map

def depth_map_to_obj(depth_map):
    """
    Converte o mapa de profundidade em um arquivo .obj (modelo 3D).
    """
    height, width = depth_map.shape
    
    vertices = []
    for y in range(height):
        for x in range(width):
            z = depth_map[y, x]
            vertices.append((x, y, z))
    
    faces = []
    for y in range(height - 1):
        for x in range(width - 1):
            v1 = y * width + x
            v2 = y * width + (x + 1)
            v3 = (y + 1) * width + x
            v4 = (y + 1) * width + (x + 1)
            faces.append((v1, v2, v3))
            faces.append((v2, v4, v3))
    
    obj_content = ""
    for v in vertices:
        obj_content += f"v {v[0]} {v[1]} {v[2]}\n"
    for f in faces:
        obj_content += f"f {f[0]+1} {f[1]+1} {f[2]+1}\n"
    
    return obj_content

def save_to_cache(image, filename):
    """
    Salva a imagem no diretório de cache.
    """
    # Converte o array numpy para uma imagem PIL
    if isinstance(image, np.ndarray):
        if image.dtype == np.float64:
            image = (image * 255).astype(np.uint8)  # Converte para uint8
        image = Image.fromarray(image)
    
    # Salva a imagem no cache
    cache_path = os.path.join(CACHE_PATH, filename)
    image.save(cache_path)