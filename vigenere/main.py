import vigenere

def main():
    while True:
        print("=== Vigenère Cipher Tool ===")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Return to Cryptography Hub")

        choice = input("Select an option: ")

        if choice == "1":
            text = input("Enter the text to encode: ")
            key = input("Enter the key: ")
            encoded_text = vigenere.vigenere_encode(text, key)
            print(f"🔒 Encoded text: {encoded_text}")

        elif choice == "2":
            text = input("Enter the encoded text: ")
            key = input("Enter the key: ")
            decoded_text = vigenere.vigenere_decode(text, key)
            print(f"🔓 Decoded text: {decoded_text}")

        elif choice == "3":
            print("Returning to Cryptography Hub...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()