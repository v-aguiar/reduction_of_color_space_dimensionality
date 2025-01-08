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

# Function that reduces the color space dimensionality of an image (color -> grayscale)
def convert_to_grayscale(img_pth):
  img = Image.open(img_pth) # Open Image
  img_array = np.array(img) # Convert Image to Array

  # Checks if the image is colored
  if len(img_array.shape) == 3:
    # Convert the image to grayscale
    gray_img = np.dot(img_array[...,:3], [0.2989, 0.5870, 0.1140])
  else:
    gray_img = img_array
  
  # Display the grayscale image
  plt.imshow(gray_img, cmap='gray')
  plt.axis('off')
  plt.show()

  return gray_img

# --------------------------- Main ---------------------------

# Upload Image
img_pth = upload_images()

# Convert Image to Grayscale
gray_img = convert_to_grayscale(img_pth)
