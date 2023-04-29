import numpy as np
import cv2

imO = cv2.imread('./images/anime/imagem2.jpg')
cv2.imshow('Imagem original', imO)
cv2.moveWindow("Imagem original", 0,0)
for x in range(0, imO.shape[1]):
    for y in range(0, imO.shape[0]):
        antesTroca = imO[x, y]
        imO[x, y] = 255 - imO[x, y]
        depoisTroca = imO[x, y]

cv2.imshow('Imagem modificada 1', imO)
cv2.moveWindow("Imagem modificada 1", imO.shape[1] * 1 + 10,0) 

for x in range(0, imO.shape[1]):
    for y in range(0, imO.shape[0]):
        imO[x, y] = 255 - imO[x, y]
      

cv2.imshow('Imagem modificada 2', imO)
cv2.moveWindow("Imagem modificada 2", imO.shape[1] * 2 + 20,0) 

cv2.waitKey(0) 
cv2.destroyAllWindows()