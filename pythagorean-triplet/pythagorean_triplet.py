#  File:       pythagorean_triplet.py
#  Purpose:    A Pythagorean triplet program
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 29 September 2016, 04:30 PM

from fractions import gcd


def triplets_in_range(min_value, max_value):
    triple = set()
    for a in range(min_value, max_value + 1):
        for b in range(a, max_value + 1):
            for c in range(b, max_value + 1):
                if a**2 + b**2 == c**2:
                    triple.update([(a, b, c)])
    return triple


def is_coprime(a, b):
    return gcd(a, b) == 1

    
