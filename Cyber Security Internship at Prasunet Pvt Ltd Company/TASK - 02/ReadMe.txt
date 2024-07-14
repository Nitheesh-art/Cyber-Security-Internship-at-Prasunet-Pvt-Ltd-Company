Pixel Manipulation for Image Encryption


To create a simple image encryption tool using pixel manipulation, we can use the Python Imaging Library (PIL) from the Pillow package. We'll perform basic operations such as swapping pixel values and applying mathematical operations to encrypt and decrypt images.

Here's a Python program to achieve this:

Install Pillow:
First, ensure you have the Pillow library installed. You can install it using 

pip install pillow

Explanation:
encrypt_image Function:

Opens the input image using Image.open().
Converts the image into a NumPy array to manipulate pixel values.
Applies encryption by performing a bitwise XOR operation between each pixel value and the provided key.
Saves the encrypted image using Image.fromarray() and save().
decrypt_image Function:

Opens the encrypted image.
Converts the image into a NumPy array.
Applies decryption by performing a bitwise XOR operation (same as encryption) between each pixel value and the provided key.
Saves the decrypted image.

main Function:

Prompts the user to choose between encryption and decryption.
Prompts the user to enter the image path, key, and output path.
Calls the encrypt_image or decrypt_image function based on the user's choice.
Prints the path of the resulting image.

Usage:
To use this program, run it and follow the prompts:

Choose to encrypt or decrypt.
Provide the path of the image you want to process.
Enter a key (integer) for encryption or decryption.
Specify the output path where the result should be saved.
This program uses a simple XOR operation for encryption and decryption. This is a basic form of encryption and may not be secure for sensitive data, but it serves as a good example of how to manipulate image pixels for this purpose.