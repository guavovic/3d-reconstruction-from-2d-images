import cv2
import torch
import matplotlib.pyplot as plt
from torchvision.transforms import ToTensor

# Carrega o modelo MiDaS (exemplo)
modelo = torch.hub.load("intel-isl/MiDaS", "MiDaS")
modelo.eval()

# Carrega a imagem
image = cv2.imread("../dados/imagens/exemplo.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
input_tensor = ToTensor()(image).unsqueeze(0)

# Estimativa de profundidade
with torch.no_grad():
    depth = modelo(input_tensor)

# Salva o mapa de profundidade
depth_map = depth.squeeze().cpu().numpy()
plt.imsave("../resultados/passo_5/mapa_profundidade.png", depth_map, cmap="plasma")

print("Mapa de profundidade salvo em resultados/passo_5/mapa_profundidade.png")