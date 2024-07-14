Implement Caesar Cipher

Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

Explanation

caesar_cipher Function:

Takes three parameters: text (the input message), shift (the shift value), and mode (either 'encrypt' or 'decrypt').
Adjusts the shift value to be within 0-25.
Changes the shift to negative for decryption.
Iterates over each character in the text:
If the character is a letter, it shifts it within the alphabet.
If the character is not a letter, it remains unchanged.
Returns the encrypted/decrypted text.

main Function:

Prompts the user to choose between encryption and decryption.
Prompts the user to enter the message and the shift value.
Calls the caesar_cipher function with the appropriate parameters.
Prints the result.

Usage

To use this program, simply run it. It will prompt you to choose between encryption and decryption, enter a message, and provide a shift value. The program will then display the encrypted or decrypted message based on your input.