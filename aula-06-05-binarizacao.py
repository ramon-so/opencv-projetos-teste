import numpy as np
import cv2

img1 = cv2.imread('./images/anime/tanjiro.jpg')
img3 = img1
img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

cv2.imshow('original', img1)

cv2.moveWindow("original", 0,0)

for x in range(0, img1.shape[0]):
    for y in range(0, img1.shape[1]):
        if((img1[x, y]) > 127):
            img3[x, y] = 255
        else:
            img3[x, y] = 0

cv2.imshow('for', img3)
cv2.moveWindow("for", 0, img1.shape[0] + 40)


#Binarização normal
limiar,img2 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)

# Binarização gauciana
img2 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                              cv2.THRESH_BINARY,15,18)

cv2.imshow('opencv', img2)
cv2.moveWindow("opencv", img1.shape[0] + 10, 0)



cv2.waitKey(0) 
cv2.destroyAllWindows()