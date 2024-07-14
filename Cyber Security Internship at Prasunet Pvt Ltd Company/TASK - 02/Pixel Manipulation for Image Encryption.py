from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = np.array(img)

    # Apply encryption: simple XOR with the key
    encrypted_pixels = pixels ^ key

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_pixels)
    encrypted_img.save(output_path)

def decrypt_image(image_path, key, output_path):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = np.array(img)

    # Apply decryption: simple XOR with the key (same as encryption)
    decrypted_pixels = pixels ^ key

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_pixels)
    decrypted_img.save(output_path)

def main():
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")

    image_path = input("Enter the path of the image: ")
    key = int(input("Enter the key (integer): "))
    output_path = input("Enter the output path: ")

    if mode == 'e':
        encrypt_image(image_path, key, output_path)
    else:
        decrypt_image(image_path, key, output_path)

    print(f"The result is saved to: {output_path}")

if __name__ == "__main__":
    main()

#COMPARE THE IMAGES

import os
from PIL import Image, ImageChops, ImageDraw
import matplotlib.pyplot as plt

def compare_images(image1_path, image2_path):
    # Check if the files exist
    if not os.path.exists(image1_path):
        print(f"File not found: {image1_path}")
        return
    if not os.path.exists(image2_path):
        print(f"File not found: {image2_path}")
        return
    
    # Open the two images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Compare the images
    diff = ImageChops.difference(image1, image2)

    # Create a new image to visualize differences
    diff_image = Image.new('RGB', (image1.width, image1.height), (255, 255, 255))
    draw = ImageDraw.Draw(diff_image)
    
    # Draw rectangles around different areas
    bbox = diff.getbbox()
   
    
    # Display the images side by side
    fig, axes = plt.subplots(1, 3, figsize=(20, 10))
    axes[0].imshow(image1)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    axes[1].imshow(image2)
    axes[1].set_title("Output Image")
    axes[1].axis('off')
    
    axes[2].imshow(diff_image)
    axes[2].set_title("Difference Image")
    axes[2].axis('off')
    
    plt.show()

# Example usage:
original_image_path = "/content/Sample.jpg"
output_image_path = "/content/rOutputSample.jpg"
compare_images(original_image_path, output_image_path)
