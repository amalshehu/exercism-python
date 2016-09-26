#  File:       simple_cipher.py
#  Purpose:    Compute the prime factors of a given natural number.
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
