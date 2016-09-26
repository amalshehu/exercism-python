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
        if not key:
            key = ''.join(random.SystemRandom().choice(ascii_lowercase) for _ in range(100))
        elif not key.isalpha() or not key.islower():
            raise ValueError('Invalid key')
        self.key = key

    def encode(self, text):
        cipher = ''
        for letter in text:
            char = (ord(letter)+self.key) % 126
            if char < 32:
                char += 31
            cipher += chr(char)
            return cipher

    def decode(self, ciph):
        txt = ''
        for item in ciph:
            t = (ord(item)-self.key) % 126
        if t < 32:
            t += 95
        txt += chr(t)
        return txt
