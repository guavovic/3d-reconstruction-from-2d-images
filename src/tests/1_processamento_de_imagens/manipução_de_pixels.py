import cv2
from matplotlib import pyplot as plt
import utils.pyplot_utils as ppu

def getColor(image, x, y):
    return image.item(y, x, 0), image.item(y, x, 1), image.item(y, x, 2)

def setColor(image, x, y, b, g, r):
    image.__setitem__((y, x, 0), b)
    image.__setitem__((y, x, 1), g)
    image.__setitem__((y, x, 2), r)
    return image

def main():
    object_image = cv2.imread('data/images/samples/opencv_banner.jpg')
    
    altura, largura, canais_de_cor = object_image.shape   
    print("Dimensões da Image: " + str(largura) + "x" + str(altura))
    print("Canais de Cor:", canais_de_cor)
    
    for y in range(0, altura):
        for x in range(0, largura):
             # print("[" + str(x) + "," + str(y) + "] = " +  str(object_image[y][x]))
             # input()
    
            azul, verde, vermelho = getColor(object_image, x, y)
            object_image = setColor(object_image, x, y, azul, verde, vermelho)
    
    eye_image = object_image[210 : 210 + 130, 265 : 265 + 140]
    cv2.imwrite("_modificada.png", object_image)
    
    object_image[100 : 100 + eye_image.shape[0], 450 : 450 + eye_image.shape[1]] = eye_image
    ppu.showImage(object_image)

if __name__ == "__main__":
    main()