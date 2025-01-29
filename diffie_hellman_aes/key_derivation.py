import os
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from key_exchange import load_dh_keys

def derive_keys():
    p, g, private_key, public_key = load_dh_keys()

    shared_key = pow(public_key, private_key, p)

    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    session_key = kdf.derive(str(shared_key).encode())

    kdf_iv = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=16,
        salt=salt,
        iterations=390000,
    )
    iv = kdf_iv.derive(str(shared_key).encode())

    with open("keys.json", "r") as f:
        keys = json.load(f)

    keys["session_key"] = session_key.hex()
    keys["iv"] = iv.hex()

    with open("keys.json", "w") as f:
        json.dump(keys, f)

    return session_key, iv