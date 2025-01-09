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
    img = Image.open(img_pth)
    img = img.convert("RGB") # Make sure the image is in RGB mode
    width, height = img.size

    grayscale_img = Image.new("L", (width, height))  # Creates a new image in grayscale mode (still blank, needs to be filled)

    # Loop through each pixel in the image
    for i in range(width):
        for j in range(height):
            r, g, b = img.getpixel((i, j))  # Get the RGB values of the pixel
            gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)  # Calculate the grayscale value of the pixel
            grayscale_img.putpixel((i, j), gray)  # Set the pixel in the new image to the grayscale value

    # Display the grayscale image
    plt.imshow(grayscale_img, cmap='gray')
    plt.axis('off')
    plt.show()

    return grayscale_img

# Function that reduces the color space dimensionality of an image (grayscale -> binary)
def convert_to_binary(grayscale_img, threshold=128):
    width, height = grayscale_img.size
    binary_img = Image.new("1", (width, height))  # Creates a new image in binary mode ("1" means one bit per pixel)

    for i in range(width):
        for j in range(height):
            gray = grayscale_img.getpixel((i, j))  # Get the grayscale value of the pixel
            binary_img.putpixel((i, j), 255 if gray > threshold else 0)  # Set the pixel in the new image to 255 (white) if the grayscale value is greater than the threshold, otherwise set it to 0 (black)

    # Display the binary image
    plt.imshow(binary_img)
    plt.axis('off')
    plt.show()

    return binary_img

# Function to save image
def save_image(img, filename):
    img.save(filename)

# Function to create download buttons
def create_download_button(gray_img, binary_img):
    root = tk.Tk()
    root.title("Download das Imagens")
    
    # Download function for grayscale image
    def on_download_gray():
        save_image(gray_img, './images/grayscale_image.png')
        print("Imagem em Tons de Cinza salva como grayscale_image.png. Você pode baixá-la agora.")
    
    # Download function for binary image
    def on_download_binary():
        save_image(binary_img, './images/binary_image.png')
        print("Imagem Binária salva como binary_image.png. Você pode baixá-la agora.")
    
    # Button to save grayscale image
    download_button_gray = tk.Button(root, text="Salvar Imagem em Tons de Cinza", command=on_download_gray)
    download_button_gray.pack(pady=10)
    
    # Button to save binary image 
    download_button_binary = tk.Button(root, text="Salvar Imagem Binária (Preto e Branco)", command=on_download_binary)
    download_button_binary.pack(pady=10)
    
    # Finish execution when closing the window
    root.protocol("WM_DELETE_WINDOW", root.quit)

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
create_download_button(gray_img, binary_img)


