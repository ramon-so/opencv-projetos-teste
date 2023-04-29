import numpy as np
import cv2

originalImage = cv2.imread('imagem2.jpg')
canalAzul, canalVerde, canalVermelho = cv2.split(originalImage)
cv2.imshow("Imagem original", originalImage) 

print(originalImage.size)
print('Largura em pixels: ', end='')
print(originalImage.shape[1]) 
print('Altura em pixels: ', end='')
print(originalImage.shape[0]) 

cv2.moveWindow("Imagem original", 40,30)  
for y in range(0, originalImage.shape[0]):
    for x in range(0, originalImage.shape[1]):
        originalImage[y, x] = 255 - originalImage[y, x]
cv2.imshow("Imagem modificada 1", originalImage)
cv2.moveWindow("Imagem modificada 1", 300,30)  

for y in range(0, originalImage.shape[0]):
    for x in range(0, originalImage.shape[1]):
        originalImage[y, x] = 255 - originalImage[y, x]
cv2.imshow("Imagem modificada 2", originalImage)
cv2.moveWindow("Imagem modificada 2", 560,30) 

for x in range(0, canalAzul.shape[1]):
    for y in range(0, canalAzul.shape[0]):
        canalAzul[x,y] = 0
cv2.imshow("canalAzul", canalAzul)
cv2.moveWindow("canalAzul", 40,290)


for x in range(0, canalVerde.shape[1]):
    for y in range(0, canalVerde.shape[0]):
        canalVerde[x,y] = 0
cv2.imshow("canalVerde", canalVerde)
cv2.moveWindow("canalVerde", 300,290)

cv2.imshow("canalVermelho", canalVermelho)
cv2.moveWindow("canalVermelho", 560,290)
 
imagemDegradeVermelho = cv2.merge((canalAzul, canalVerde, canalVermelho))
cv2.imshow("imagem degrade", imagemDegradeVermelho)
cv2.moveWindow("imagem degrade", 40, 600)

cv2.waitKey(0) 
cv2.destroyAllWindows()