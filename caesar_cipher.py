def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # same logic with negative shift

def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            encrypted = caesar_encrypt(message, shift)
            print("🔐 Encrypted Message:", encrypted)

        elif choice == '2':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            decrypted = caesar_decrypt(message, shift)
            print("🔓 Decrypted Message:", decrypted)

        elif choice == '3':
            print("Exiting Caesar Cipher Tool. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
