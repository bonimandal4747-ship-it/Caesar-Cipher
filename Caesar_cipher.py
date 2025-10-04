# Caesar Cipher in Python

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # shift character and wrap around using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # non-letters remain unchanged
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # decryption is just reverse shift


# Main program
if __name__ == "__main__":
    print("=== Caesar Cipher Program ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g. 3): "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted message:", encrypted)
    print("Decrypted message:", decrypted)
