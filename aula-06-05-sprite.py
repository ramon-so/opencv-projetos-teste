import numpy as np
import cv2

limiar = 1

while(limiar > 0):
    limiar = int(input("Informe o limiar: "))
    img1 = cv2.imread('./images/anime/inosuke.jpg')
    img3 = img1
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

    cv2.imshow('original', img1)

    cv2.moveWindow("original", 0,0)

    for x in range(0, img1.shape[0]):
        for y in range(0, img1.shape[1]):
            if((img1[x, y]) > 127):
                img3[x, y] = int(img3[x, y]) + limiar if int(img3[x, y]) + limiar < 255 else 255
            else:
                img3[x, y] = int(img3[x, y]) - limiar if int(img3[x, y]) - limiar > 0 else 0
    cv2.imshow('for', img3)
    cv2.moveWindow("for", 0, img1.shape[0] + 40)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()