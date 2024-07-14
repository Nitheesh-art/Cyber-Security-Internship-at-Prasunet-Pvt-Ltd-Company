def caesar_cipher(text, shift, mode='encrypt'):
    # Ensure the shift value is within 0-25
    shift = shift % 26
    
    if mode == 'decrypt':
        shift = -shift
    
    encrypted_text = ''
    
    for char in text:
        if char.isalpha():
            # Shift character within the alphabet
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += new_char
        else:
            # Leave non-alphabet characters unchanged
            encrypted_text += char
    
    return encrypted_text

def main():
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
    
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if mode == 'e':
        result = caesar_cipher(text, shift, 'encrypt')
    else:
        result = caesar_cipher(text, shift, 'decrypt')
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
