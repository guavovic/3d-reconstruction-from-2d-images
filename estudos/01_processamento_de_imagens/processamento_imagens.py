import cv2
import estudos.config as config

image = cv2.imread(str(config.PASTA_IMAGENS / "exemplo.jpg"))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

print("Processamento de imagens concluído!")