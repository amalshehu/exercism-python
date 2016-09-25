#  File:       prime_factors.py
#  Purpose:    Compute the prime factors of a given natural number.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Monday 26 September 2016, 12:05 AM


def prime(number):
    if number <= 1:
        return False
    else:
        if number % 1 == 0 and number % range(2, number)
