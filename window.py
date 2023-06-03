from tkinter import *
from matplotlib import pyplot as plt
import numpy as np
import cv2

def ShowNegative():
    cv2.destroyAllWindows()
    imagem = cv2.imread('./images/anime/inosuke.jpg')
    cv2.imshow('Original', imagem)
    cv2.moveWindow("Original", 0,0)

    for x in range(0, imagem.shape[1]):
        for y in range(0, imagem.shape[0]):
            antesTroca = imagem[x, y]
            imagem[x, y] = 255 - imagem[x, y]
            depoisTroca = imagem[x, y]

    cv2.imshow('Negativo', imagem)
    cv2.moveWindow("Negativo", imagem.shape[1] * 1 + 10,0) 

def ShowAdd():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/tanjiro.jpg')
    img2 = cv2.imread('./images/anime/inosuke.jpg')

    cv2.imshow('Imagem 1', img1)
    cv2.imshow('Imagem 2', img2)

    cv2.moveWindow("Imagem 1", 0,0)
    cv2.moveWindow("Imagem 2", img2.shape[1] + 10, 0)

    img3 = cv2.add(img1, img2)
    cv2.imshow('sum opencv', img3)
    cv2.moveWindow("sum opencv", img2.shape[1] * 2 + 20 , 0) 

def ShowSub():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/tanjiro.jpg')
    img2 = cv2.imread('./images/anime/inosuke.jpg')

    cv2.imshow('Imagem 1', img1)
    cv2.imshow('Imagem 2', img2)

    cv2.moveWindow("Imagem 1", 0,0)
    cv2.moveWindow("Imagem 2", img2.shape[1] + 10, 0)

    img3 = cv2.subtract(img1, img2)
    cv2.imshow('sum opencv', img3)
    cv2.moveWindow("sum opencv", img2.shape[1] * 2 + 20 , 0) 

def ShowChanels():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/inosuke.jpg') 
    canalAzul, canalVerde, canalVermelho = cv2.split(img1)

    cv2.imshow('Original', img1)
    cv2.imshow('Azul', canalAzul)
    cv2.imshow('Verde', canalVerde)
    cv2.imshow('Vermelho', canalVermelho)

    cv2.moveWindow("Original", img1.shape[1] + 10, 0)
    cv2.moveWindow("Azul", img1.shape[1] * 2 + 20 , 0) 
    cv2.moveWindow("Verde", img1.shape[1] * 3 + 30 , 0)
    cv2.moveWindow("Vermelho", img1.shape[1] * 4 + 40 , 0)  

def ShowBinary():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/inosuke.jpg') 
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Original', img1)
    cv2.moveWindow("Original", img1.shape[1] + 10, 0) 

    ret,img2 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
    cv2.imshow('Binary', img2)
    cv2.moveWindow("Binary", img1.shape[1] * 2 + 20, 0) 

def ShowSpliting():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/inosuke.jpg')
    img3 = img1
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

    cv2.imshow('original', img1)

    cv2.moveWindow("original", 0,0)

    for x in range(0, img1.shape[0]):
        for y in range(0, img1.shape[1]):
            if((img1[x, y]) > 127):
                img3[x, y] = int(img3[x, y]) + 30 if int(img3[x, y]) + 30 < 255 else 255
            else:
                img3[x, y] = int(img3[x, y]) - 30 if int(img3[x, y]) - 30 > 0 else 0
    cv2.imshow('for', img3)
    cv2.moveWindow("for", 0, img1.shape[0] + 40)

def ShowAvarage():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/tanjiro.jpg') 
    cv2.imshow('Original', img1)
    cv2.moveWindow("Original", img1.shape[1] + 10, 0) 

    median = cv2.blur(img1,ksize=(3,3))
    cv2.imshow('Media', median)
    cv2.moveWindow("Media", img1.shape[1] * 2 + 20, 0) 

def ShowMedian():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/tanjiro.jpg') 
    cv2.imshow('Original', img1)
    cv2.moveWindow("Original", img1.shape[1] + 10, 0) 

    median = cv2.medianBlur(img1, 3)
    cv2.imshow('Media', median)
    cv2.moveWindow("Media", img1.shape[1] * 2 + 20, 0) 

def ShowSobel():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/tanjiro.jpg') 
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    ret,img2 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
    cv2.imshow('Original', img2)
    cv2.moveWindow("Original", img1.shape[1] + 10, 0) 

    sobel8u = cv2.Sobel(img2, cv2.CV_8U,1,0,ksize=3)
    cv2.imshow('Sobel 8u', sobel8u)
    cv2.moveWindow("Sobel 8u", img1.shape[1] * 2 + 20, 0) 

    sobel64F = cv2.Sobel(img2, cv2.CV_64F,1,0,ksize=3)
    cv2.imshow('Sobel 64F', sobel64F)
    cv2.moveWindow("Sobel 64F", img1.shape[1] * 3 + 30, 0) 

def ShowHist():
    cv2.destroyAllWindows()
    img1 = cv2.imread('./images/anime/tanjiro.jpg') 
    cv2.imshow('Original', img1)
    cv2.moveWindow("Original", img1.shape[1] + 10, 0) 

    histb = cv2.calcHist([img1],[0],None,[256],[0,256])
    histg = cv2.calcHist([img1],[1],None,[256],[0,256])
    histr = cv2.calcHist([img1],[2],None,[256],[0,256])
    plt.plot(histb, color='b')
    plt.plot(histg, color='g')
    plt.plot(histr, color='r')
    plt.title('Image Histogram')
    plt.show()

gui = Tk()
gui.title("Opencv Functions")

btn = Button(gui, text="Negativo", command=ShowNegative)
btn2 = Button(gui, text="Adição", command=ShowAdd)
btn3 = Button(gui, text="Subtração", command=ShowSub)
btn4 = Button(gui, text="Separação de canais", command=ShowChanels)
btn5 = Button(gui, text="Binarização", command=ShowBinary)
btn6 = Button(gui, text="Spliting", command=ShowSpliting)
btn7 = Button(gui, text="Média", command=ShowAvarage)
btn8 = Button(gui, text="Mediana", command=ShowMedian)
btn9 = Button(gui, text="Solbel", command=ShowSobel)
btn10 = Button(gui, text="Histograma", command=ShowHist)
btn11 = Button(gui, text="Quantização", command=ShowMedian)
btn12 = Button(gui, text="Equalização", command=ShowSobel)

btn.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=0, column=3)
btn5.grid(row=0, column=4)
btn6.grid(row=0, column=5)
btn7.grid(row=0, column=6)
btn8.grid(row=0, column=7)
btn9.grid(row=0, column=8)
btn10.grid(row=0, column=9)
btn11.grid(row=0, column=10)
btn12.grid(row=0, column=11)

button_width = btn.winfo_reqwidth() + btn2.winfo_reqwidth()+btn3.winfo_reqwidth()+ btn4.winfo_reqwidth()+ btn5.winfo_reqwidth()+ btn6.winfo_reqwidth()+ btn7.winfo_reqwidth()+ btn8.winfo_reqwidth()+ btn9.winfo_reqwidth()+ btn10.winfo_reqwidth()+ btn11.winfo_reqwidth()+ btn12.winfo_reqwidth()
button_height = max(btn.winfo_reqheight(), btn2.winfo_reqheight(), btn3.winfo_reqheight(), btn4.winfo_reqheight(), btn5.winfo_reqheight(), btn6.winfo_reqheight(), btn7.winfo_reqheight(), btn8.winfo_reqheight())

window_width = button_width
window_height = button_height * 2
gui.geometry(f"{window_width}x{window_height}")

gui.mainloop()

