from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import cv2
from skimage.segmentation import chan_vese
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.segmentation import chan_vese


def mumford_shah_segmentation():
    cv2.destroyAllWindows()
    path = GetImageOne()
    path = path[0]
    print(path)
    image = cv2.imread(path, 0)  
    
    image = img_as_float(image)
    # Feel free to play around with the parameters to see how they impact the result
    cv = chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                max_num_iter=200, dt=0.5, init_level_set="checkerboard",
                extended_output=True)

    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    ax = axes.flatten()

    ax[0].imshow(image, cmap="gray")
    ax[0].set_axis_off()
    ax[0].set_title("Original Image", fontsize=12)

    ax[1].imshow(cv[0], cmap="gray")
    ax[1].set_axis_off()
    title = f'Chan-Vese segmentation - {len(cv[2])} iterations'
    ax[1].set_title(title, fontsize=12)

    ax[2].imshow(cv[1], cmap="gray")
    ax[2].set_axis_off()
    ax[2].set_title("Final Level Set", fontsize=12)

    ax[3].plot(cv[2])
    ax[3].set_title("Evolution of energy over iterations", fontsize=12)

    fig.tight_layout()
    plt.show()

def GetImageOne():
    root = Tk()
    root.withdraw()

    arquivos_imagem = filedialog.askopenfilenames(
        title="Selecione uma imagens:",
        filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"), ("Todos os arquivos", "*.*")),
        multiple=False
    )

    return arquivos_imagem

gui = Tk()
gui.title("Segmentação por Crescimento de região Mumford-Shah")

btn = Button(gui, text="Segmentação Mumford-Shah", command=mumford_shah_segmentation)
btn.grid(row=0, column=0)
button_width = btn.winfo_reqwidth()
button_height = btn.winfo_reqheight()

window_width = 500
window_height = button_height
gui.geometry(f"{window_width}x{window_height}")

gui.mainloop()
