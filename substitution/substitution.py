import string
import json
import os

CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits

def encode_substitution(text, substitution_key):
    mapping = str.maketrans(CHARACTERS, substitution_key)
    return text.translate(mapping)

def decode_substitution(text, substitution_key):
    inverse_mapping = str.maketrans(substitution_key, CHARACTERS)
    return text.translate(inverse_mapping)

def save_key(substitution_key, filename="keys.json"):
    keys = {"substitution_key": substitution_key}
    with open(filename, "w") as f:
        json.dump(keys, f)

def load_key(filename="keys.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            keys = json.load(f)
            return keys.get("substitution_key")
    return None