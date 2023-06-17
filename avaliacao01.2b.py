from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import cv2

def ShowBinary(limiar, tolerancia12):
    cv2.destroyAllWindows()
    
    path = GetImageOne()
    path = path[0]
    print(path)
    img1 = cv2.imread(path) 
    cv2.imshow('Original', img1)
    improc = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    for x in range(0, improc.shape[0]):
        for y in range(0, improc.shape[1]):
            if((int(improc[x, y])) < (limiar + tolerancia) and (int(improc[x, y])) > (limiar - tolerancia)):
                improc[x, y] = 255
            else:
                improc[x, y] = 0
    cv2.imshow('binarizada', improc)
    cv2.moveWindow("binarizada", 0, improc.shape[0] + 40)

def GetImageOne():
    root = Tk()
    root.withdraw()

    arquivos_imagem = filedialog.askopenfilenames(
        title="Selecione uma imagens:",
        filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"), ("Todos os arquivos", "*.*")),
        multiple=False
    )

    return arquivos_imagem

limiar = int(input('Selecione o limiar: '))
tolerancia = int(input('Selecione a tolerancia: '))

gui = Tk()
gui.title("Binarização por limiar")

btn = Button(gui, text="Binarizar por limiar", command=ShowBinary(limiar, tolerancia))
btn.grid(row=0, column=0)
button_width = btn.winfo_reqwidth()
button_height = btn.winfo_reqheight()

window_width = 500
window_height = button_height
gui.geometry(f"{window_width}x{window_height}")

gui.mainloop()