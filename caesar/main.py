import caesar

def main():
    while True:
        print("=== Caesar Cipher Tool ===")
        print("1. Encode a message")
        print("2. Decode a message (Brute-force)")
        print("3. Return to Cryptography Hub")

        choice = input("Select an option: ")

        if choice == "1":
            text = input("Enter the text to encode: ")
            shift = int(input("Enter the shift value: "))
            encoded_text = caesar.caesar_encode(text, shift)
            print(f"🔒 Encoded text: {encoded_text}")

        elif choice == "2":
            text = input("Enter the encoded text: ")
            print("\n🔓 Possible decodings:")
            decoded_results = caesar.caesar_decode(text)
            for shift, decoded_text in decoded_results.items():
                print(f"Shift {shift}: {decoded_text}")

        elif choice == "3":
            print("Returning to Cryptography Hub...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()