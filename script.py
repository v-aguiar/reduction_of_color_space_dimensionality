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

# Function that reduces the color space dimensionality of an image (grayscale -> binary)
def convert_to_binary(gray_img, threshold=128):
  # Convert the grayscale image to binary
  binary_img = np.where(gray_img > threshold, 255, 0)

  # Display the binary image
  plt.imshow(binary_img, cmap='gray')
  plt.axis('off')
  plt.show()

  return binary_img

# Function to save image
def save_image(img, filename):
    Image.fromarray(img.astype(np.uint8)).save(filename)

# Function that allows the user to download the image
def create_download_button(binary_img, filename):
    root = tk.Tk()
    root.title("Download da Imagem")
    
    # Download function
    def on_download():
        save_image(binary_img, filename)
        print(f"Imagem salva como {filename}. Você pode baixá-la agora.")
        root.quit()  # Close window after download
    
    # Create download button
    download_button = tk.Button(root, text="Salvar Imagem em Preto e Branco", command=on_download)
    download_button.pack(pady=20)
    
    # Starts UI
    root.mainloop()

# --------------------------- Main ---------------------------

# Upload Image
img_pth = upload_images()

# Convert Image to Grayscale
gray_img = convert_to_grayscale(img_pth)

# Convert Image to Binary
binary_img = convert_to_binary(gray_img)

# Download Image
create_download_button(binary_img, 'binary_image.jpg')

