import string

CHARACTERS = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digits": string.digits
}

def caesar_encode(text, shift):
    def shift_char(c, n):
        for key, character in CHARACTERS.items():
            if c in character:
                return character[(character.index(c) + n) % len(character)]
        return c

    return ''.join(shift_char(c, shift) for c in text)

def caesar_decode(text):
    def shift_char(c, n):
        for key, character in CHARACTERS.items():
            if c in character:
                return character[(character.index(c) - n) % len(character)]
        return c

    results = {}
    for shift in range(1, 26):
        decoded_text = ''.join(shift_char(c, shift) for c in text)
        results[shift] = decoded_text
    return results