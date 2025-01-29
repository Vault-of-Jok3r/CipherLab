import substitution

def main():
    while True:
        print("=== Substitution Cipher Tool ===")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Return to Cryptography Hub")

        choice = input("Select an option: ")

        if choice == "1":
            key = input("Enter the substitution key: ")
            text = input("Enter the text to encode: ")
            encoded_text = substitution.encode_substitution(text, key)
            print(f"🔒 Encoded text: {encoded_text}")

        elif choice == "2":
            key = input("Enter the substitution key: ")
            text = input("Enter the encoded text: ")
            decoded_text = substitution.decode_substitution(text, key)
            print(f"🔓 Decoded text: {decoded_text}")

        elif choice == "3":
            print("Returning to Cryptography Hub...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()