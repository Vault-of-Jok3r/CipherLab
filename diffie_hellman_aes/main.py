import key_exchange
import key_derivation
import encryption

def main():
    while True:
        print("=== Diffie-Hellman + AES Encryption Tool ===")
        print("1. Generate and exchange keys")
        print("2. Derive session key and IV")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Return to Cryptography Hub")

        choice = input("Select an option: ")

        if choice == "1":
            key_exchange.generate_dh_keys()
            print("✔ Diffie-Hellman keys generated and saved.")
        elif choice == "2":
            key_derivation.derive_keys()
            print("✔ AES key and IV derived and saved.")
        elif choice == "3":
            message = input("Enter the message to encrypt: ")
            encrypted_text = encryption.encrypt(message)
            print(f"🔒 Encrypted message: {encrypted_text}")
        elif choice == "4":
            encrypted_text = input("Enter the encrypted message: ")
            decrypted_message = encryption.decrypt(encrypted_text)
            print(f"🔓 Decrypted message: {decrypted_message.decode()}")
        elif choice == "5":
            print("Returning to Cryptography Hub...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()