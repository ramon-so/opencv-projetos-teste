import numpy as np
import cv2

img1 = cv2.imread('./images/anime/tanjiro.jpg')
img2 = cv2.imread('./images/anime/inosuke.jpg')
img4 = img1
img5 = img1

img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

cv2.imshow('Imagem original tanjiro', img1)
cv2.imshow('Imagem original inosuke', img2)

cv2.moveWindow("Imagem original tanjiro", 0,0)
cv2.moveWindow("Imagem original inosuke", img2.shape[1] + 10, 0)

img3 = cv2.add(img1, img2)

for x in range(0, img1.shape[0]):
    for y in range(0, img1.shape[1]):
        if((img1[x, y] + img2[x, y]) > 255):
            img4[x, y] = 255
        else:
            img4[x, y] = img1[x, y] + img2[x, y]

cv2.imshow('sum opencv', img3)
cv2.moveWindow("sum opencv", img2.shape[1] + 10, img1.shape[0] + 40) 

cv2.imshow('sum for unit8', img4)
cv2.moveWindow("sum for unit8", 0, img1.shape[0] + 40) 

for x in range(0, img1.shape[0]):
    for y in range(0, img1.shape[1]):
        if((int(img1[x, y]) + int(img2[x, y])) > 255):
            img5[x, y] = 255
        else:
            img5[x, y] = int(img1[x, y]) + int(img2[x, y])

cv2.imshow('sum for int', img5)
cv2.moveWindow("sum for int", 0, img1.shape[0] *2 + 80) 

cv2.waitKey(0) 
cv2.destroyAllWindows()