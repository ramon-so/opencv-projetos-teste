from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import cv2

def ShowBinary():
    cv2.destroyAllWindows()
    path = GetImageOne()
    path = path[0]
    print(path)
    img1 = cv2.imread(path) 
    cv2.imshow('Original', img1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    cv2.moveWindow("Original", img1.shape[1] + 10, 0) 

    ret,img2 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
    cv2.imshow('Binary', img2)
    cv2.moveWindow("Binary", img1.shape[1] * 2 + 20, 0) 

    countPixels(img2)

def GetImageOne():
    root = Tk()
    root.withdraw()

    arquivos_imagem = filedialog.askopenfilenames(
        title="Selecione uma imagens:",
        filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"), ("Todos os arquivos", "*.*")),
        multiple=False
    )

    return arquivos_imagem

def countPixels(img2):
    count = 0
    for x in range(0, img2.shape[0]-1):
        for y in range(0, img2.shape[1]-1):
            if(img2[x, y] != 0):
                count += 1
    
    print('A quantidade de pixels pretos é: ', count, ' pixels')

gui = Tk()
gui.title("Contagem pixels pretos em imagem binarizada")

btn = Button(gui, text="Binarizar e contar pixels", command=ShowBinary)
btn.grid(row=0, column=0)
button_width = btn.winfo_reqwidth()
button_height = btn.winfo_reqheight()

window_width = 500
window_height = button_height
gui.geometry(f"{window_width}x{window_height}")

gui.mainloop()