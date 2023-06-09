import numpy as np
import cv2

originalImage = cv2.imread('./images/satellite/imagem6.PNG')
canalAzul, canalVerde, canalVermelho = cv2.split(originalImage)

for y in range(0, canalAzul.shape[1]):
    for x in range(0, canalAzul.shape[0]):
        if(canalAzul[x, y] < canalVerde[x, y] + 50 and canalAzul[x, y] < canalVermelho[x, y] + 50):
            canalVerde[x,y] = 0
            canalVermelho[x,y] = 0
            canalAzul[x,y] = 0

cv2.imshow("Imagem original", originalImage) 
cv2.moveWindow("Imagem original", 0, 0)

imagemTratada = cv2.merge((canalAzul, canalVerde, canalVermelho))
imagemTratada = cv2.medianBlur(imagemTratada, 5)

canalAzul, canalVerde, canalVermelho = cv2.split(imagemTratada)

for y in range(0, canalAzul.shape[1]):
    for x in range(0, canalAzul.shape[0]):
        if(canalAzul[x, y] != 0 and canalAzul[x, y] < 100):
            canalVerde[x,y] = 0
            canalVermelho[x,y] = 0
            canalAzul[x,y] = 225
        
imagemTratada = cv2.merge((canalAzul, canalVerde, canalVermelho))

imagemTratada = cv2.Canny(imagemTratada, 70, 150)

(lx, objetos) = cv2.findContours(imagemTratada.copy(),
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(str(len(objetos[0])))


cv2.imshow("imagem tratada", imagemTratada)
cv2.moveWindow("imagem tratada", originalImage.shape[1] + 10, 0)

cv2.waitKey(0) 
cv2.destroyAllWindows()