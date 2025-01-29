import os

def run_tool(tool_path):
    os.system(f"python {tool_path}")

def main():
    while True:
        print("\n=== Cryptography Tool Hub ===")
        print("1. Vigenère Cipher")
        print("2. Substitution Cipher")
        print("3. Caesar Cipher")
        print("4. Diffie-Hellman + AES Encryption")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            run_tool("vigenere/main.py")
        elif choice == "2":
            run_tool("substitution/main.py")
        elif choice == "3":
            run_tool("caesar/main.py")
        elif choice == "4":
            run_tool("diffie_hellman_aes/main.py")
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()