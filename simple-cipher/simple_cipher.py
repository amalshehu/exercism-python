import random
from string import ascii_lowercase

letters = ascii_lowercase


class Cipher():
    """Generate a key for Cipher if not provided."""
    def __init__(self, key=None):

        if not key:
            key = ''.join(random.SystemRandom().choice(ascii_lowercase) for _ in range(150))
        elif not key.isalpha() or not key.islower():
            raise ValueError('Invalid key')
        self.key = key

    def encode(self, text):
            key = self.key
            while len(key) < len(text):
                key += self.key
            cipher = ""
            for i in range(len(text)):
                letter = text.lower()[i]
                if letter in letters:
                    cipher += letters[(letters.index(letter)+letters.index(key[i])) % 26]
            return cipher

    def decode(self, ciph):
        key = self.key
        while len(key) < len(ciph):
            key += self.key
        txt = ""
        for i in range(len(ciph)):
            letter = ciph.lower()[i]
            if letter in letters:
                txt += letters[(letters.index(letter)-letters.index(key[i])) % 26]
        return txt


class Caesar():

    def encode(self, text):
        return ''.join([letters[(letters.index(letter)+3) % 26] \
                for letter in text.lower() if letter in letters])

    def decode(self, ciph):
        return ''.join([letters[(letters.index(letter)-3) % 26] \
                for letter in ciph.lower() if letter in letters])
