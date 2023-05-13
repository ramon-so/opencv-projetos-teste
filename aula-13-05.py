import numpy as np
import cv2

def bubbleSort(lista):
    ordened = False
    while (not ordened):
        for i in range(len(lista) -1 ):
            if (lista[i] > lista[i + 1]):
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                ordened = False
                break
            ordened = True
    return lista


img1 = cv2.imread('./images/anime/tanjiro.jpg')
img3 = img1
listaNova = img3
img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
listaNova = cv2.cvtColor(listaNova, cv2.COLOR_RGB2GRAY)
img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

cv2.imshow('original', img1)

cv2.moveWindow("original", 0,0)

soma = 0
for x in range(0, img1.shape[0]-1):
    for y in range(0, img1.shape[1]-1):
        if(not(x == 0 or x == img1.shape[0]-1 or y == 0 or y == img1.shape[1] -1)):
            lista = [img1[x+1, y], img1[x-1, y], img1[x, y+1], img1[x, y-1], img1[x+1, y-1], img1[x+1, y+1], img1[x-1, y-1], img1[x-1, y+1], img1[x,y]]
            lista = bubbleSort(lista)
            
            img3[x, y] = (lista[5])
        soma = int(img1[x+1, y]) + int(img1[x-1, y]) + int(img1[x, y+1]) + int(img1[x, y-1]) + int(img1[x+1, y-1]) + int(img1[x+1, y+1]) + int(img1[x-1, y-1]) + int(img1[x-1, y+1]) + int(img1[x,y])
        listaNova[x,y] = round( soma / 9)
img3 = cv2.adaptiveThreshold(img3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                              cv2.THRESH_BINARY,15,18)
listaNova = cv2.adaptiveThreshold(listaNova,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                              cv2.THRESH_BINARY,15,18)
cv2.imshow('media', listaNova)
cv2.moveWindow("media", img1.shape[0] + 10, 0)
cv2.imshow('mediana', img3)
cv2.moveWindow("mediana", img1.shape[0] * 2 + 20, 0)
cv2.waitKey(0) 
cv2.destroyAllWindows()



    
