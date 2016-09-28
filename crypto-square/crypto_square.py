#  File:       crypto_square.py
#  Purpose:    Implement the method for composing secret messages called a square code.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Tuesday 28 September 2016, 03:27 PM
from math import ceil, sqrt
from itertools import izip_longest


def normalize(message):
    return ''.join([i for i in message if i.isalnum()]).lower()


def text_square(text, num):
    if len(text) <= num:
        return [text]
    return [text[:num]] + text_square(text[num:], num)


def encode(text):
    text = normalize(text)
    side = int(ceil(sqrt(len(text))))
    clip = text_square(text, side)
    return ' '.join([''.join(col)for col in izip_longest(*clip, fillvalue='')])
