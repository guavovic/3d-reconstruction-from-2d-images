import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../dados/imagens/exemplo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

print("Processamento de imagens concluído!")