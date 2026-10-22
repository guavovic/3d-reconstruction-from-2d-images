import os
import cv2
import estudos.config as config
import torch
import matplotlib.pyplot as plt
from torchvision.transforms import ToTensor

def main():
    # Load a model (see https://github.com/intel-isl/MiDaS/#Accuracy for an overview)
    model_type = 'DPT_Large'
    midas = torch.hub.load('intel-isl/MiDaS', model_type)

    # Move model to GPU if available
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    midas.to(device)
    midas.eval()

    # Load transforms to resize and normalize the image for large or small model
    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

    if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
        transform = midas_transforms.dpt_transform
    else:
        transform = midas_transforms.small_transform

    # Load image and apply transforms
    image = cv2.imread(os.path.join(config.pasta_resultados('02_deteccao_de_contornos', 'remocao_de_fundo'), 'rembg_grabcut.png'))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    input_batch = transform(image).to(device)
    # input_batch = ToTensor()(image).unsqueeze(0)

    # Predict and resize to original resolution
    with torch.no_grad():
        prediction = midas(input_batch)

        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=image.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    depth_map = prediction.cpu().numpy()

    path = os.path.join(config.pasta_resultados('04_estimativa_de_profundidade'), 'mapa_profundidade.png')
    plt.imsave(path, depth_map, cmap='plasma')

    print('Mapa de profundidade salvo em ' +  path)
    
if __name__ == "__main__":
    main()