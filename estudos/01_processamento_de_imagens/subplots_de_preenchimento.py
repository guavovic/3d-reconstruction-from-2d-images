import numpy as np
import cv2
import estudos.utils as utils
import estudos.config as config

def plotTwoImageVertical(imageOriginal):
    imgReplicate = cv2.copyMakeBorder(imageOriginal, 200, 100, 50, 10, cv2.BORDER_REPLICATE)

    # criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imageOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    utils.showMultipleImageGrid(imgsArray, title, 1, 2)

def plotTwoImageHorizontal(imageOriginal):
    imgReplicate = cv2.copyMakeBorder(imageOriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

    # criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imageOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    utils.showMultipleImageGrid(imgsArray, title, 2, 1)

def plotThreeImages(imageOriginal):
    imgReplicate = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgTransparent = np.ones((imageOriginal.shape[0], imageOriginal.shape[1], 4), np.uint8) * 255

    # criando grid com 3 imagens, a segunda com borda replicada e a terceira com borda de espelho
    # a ultima imagem é transparente
    imgsArray = [imageOriginal, imgReplicate, imgReflect, imgTransparent]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', '']
    utils.showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def plotFourImages(imageOriginal):
    imgReplicate = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)

    # criando grid com 4 imagens, a segunda com borda replicada e a terceira e quarta com borda de espelho
    imgsArray = [imageOriginal, imgReplicate, imgReflect, imgReflect101]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 2']
    utils.showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def plotSixImages(imageOriginal):
    imgReplicate = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
    imgWrap = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_WRAP)

    BLUE = [255, 0, 0]
    imgConstant = cv2.copyMakeBorder(imageOriginal, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value = BLUE)

    # criando grid com 6 imagens, a segunda com borda replicada e a terceira e quarta com borda de espelho
    # constant insere uma moldura e wrap só olhando pra entender =)
    imgsArray = [imageOriginal, imgReplicate, imgReflect, imgReflect101, imgConstant, imgWrap]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 2', 'Moldura', 'Efeito Wrap']
    utils.showMultipleImageGrid(imgsArray, titlesArray, 3, 2)

def main():
    object_image = cv2.imread(str(config.PASTA_IMAGENS / 'opencv_banner_fundo_branco.jpg'))
    
    plotTwoImageVertical(object_image)
    plotTwoImageHorizontal(object_image)
    plotThreeImages(object_image)
    plotFourImages(object_image)
    plotSixImages(object_image)

if __name__ == "__main__":
    main()