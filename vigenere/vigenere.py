import string

CHARACTER_SET = string.ascii_lowercase + string.ascii_uppercase + string.digits

def vigenere_shift(char, shift_char, encode=True):
    if char in CHARACTER_SET:
        shift = CHARACTER_SET.index(shift_char)
        shift = shift if encode else -shift
        return CHARACTER_SET[(CHARACTER_SET.index(char) + shift) % len(CHARACTER_SET)]
    return char

def vigenere_encode(text, key):
    repeated_key = (key * (len(text) // len(key) + 1))[:len(text)]
    return "".join(vigenere_shift(text[i], repeated_key[i], encode=True) for i in range(len(text)))

def vigenere_decode(encoded_text, key):
    repeated_key = (key * (len(encoded_text) // len(key) + 1))[:len(encoded_text)]
    return "".join(vigenere_shift(encoded_text[i], repeated_key[i], encode=False) for i in range(len(encoded_text)))