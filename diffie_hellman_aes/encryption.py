import json
import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def load_keys():
    with open("keys.json", "r") as f:
        keys = json.load(f)

    session_key = bytes.fromhex(keys["session_key"])
    iv = bytes.fromhex(keys["iv"])
    return session_key, iv

def encrypt(plaintext):
    session_key, iv = load_keys()
    cipher = Cipher(algorithms.AES(session_key), modes.CTR(iv))
    encryptor = cipher.encryptor()
    return binascii.b2a_hex(encryptor.update(plaintext.encode()) + encryptor.finalize()).decode()

def decrypt(ciphertext):
    session_key, iv = load_keys()
    cipher = Cipher(algorithms.AES(session_key), modes.CTR(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(binascii.a2b_hex(ciphertext)) + decryptor.finalize()