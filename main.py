import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encoder(message: str, encoder: str, key=1) -> str:
    """
    Returns the encoded message using the given encoder (and key if needed).
    """
    pass


def _typewriter(message: str, alphabet_from: list, alphabet_to: list):
    encoded_message = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet_from.index(letter)
            encoded_message += alphabet_to[position]
        elif letter.lower() in alphabet:
            position = alphabet_from.index(letter.lower())
            encoded_message += alphabet_to[position].upper()
        else:
            encoded_message += letter
    return encoded_message


def caesar(message: str, key: int) -> str:
    alpha1 = alphabet[key % 26:] + alphabet[:key % 26]
    return _typewriter(message, alphabet, alpha1)


def substitution(message: str) -> str:
    alpha1 = alphabet.copy()
    random.shuffle(alpha1)
    return _typewriter(message, alphabet, alpha1)


def vigenere(message:str, codeword:str) -> str:
    dict = {}
    codeword.lower()
    code_no_dupes = "".join(set(codeword))
    for letter in code_no_dupes:
        key = alphabet.index(letter)
        alpha1 = alphabet[key % 26:] + alphabet[:key % 26]
        dict[letter] = alpha1
    message.replace(" ", "")
    pass


def decoder(message: str):
    pass


def caesar_decode(message: str, key: int) -> str:
    alpha1 = alphabet[key % 26:] + alphabet[:key % 26]
    return _typewriter(message, alpha1, alphabet)


if __name__ == '__main__':
    encoded = caesar("Fuck the world", 4)
    print(encoded)
    decoded = caesar_decode(encoded, 4)
    print(decoded)
