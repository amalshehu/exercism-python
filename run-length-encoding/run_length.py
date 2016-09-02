#  File:       run_length.py
#  Purpose:    Implement run-length encoding and decoding.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 09:10 PM

from re import sub


def encode(text):
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), text)


def decode(text):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), text)
