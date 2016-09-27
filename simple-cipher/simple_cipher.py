#  File:       simple_cipher.py
#  Purpose:    Implement a simple shift cipher like Caesar and a more secure substitution cipher
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Monday 26 September 2016, 02:00 AM

import random
from string import ascii_lowercase


class Cipher():
    """Generate a key for Cipher if not provided."""
    def __init__(self, key=None):
        self.letters = ascii_lowercase
        if not key:
            key = ''.join(random.SystemRandom().choice(ascii_lowercase) for _ in range(150))
        elif not key.isalpha() or not key.islower():
            raise ValueError('Invalid key')
        self.key = key

    def encode(self, text):
            while len(key) < len(text):
                key += self.key
            cipher = ""
            for i in range(len(text)):
                letter = text.lower()[i]
                if letter in self.letters:
                    cipher += self.letters[(self.letters.index(letter)+self.letters.index(key[i]))%26]
            return cipher

    def decode(self, ciph):
        while len(key) < len(ciph):
            key += self.key
        txt = ""
        for i in range(len(ciph)):
            letter = ciph.lower()[i]
            if letter in self.letters:
                txt += self.letters[(self.letters.index(letter)-self.letters.index(key[i]))%26]
        return txt
