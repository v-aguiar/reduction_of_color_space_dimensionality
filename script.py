import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Function for uploading images
def upload_images():
    root = tk.Tk()
    root.withdraw()

    img_pth = filedialog.askopenfilename(title='Selecione uma imagem', filetypes=[('Imagens', '*.png *.jpg *.jpeg *.bmp')])

    # Open image
    img = Image.open(img_pth)
    img = np.array(img)

    # Show image
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    return img_pth

# --------------------------- Main ---------------------------

# Upload Image
img_pth = upload_images()
