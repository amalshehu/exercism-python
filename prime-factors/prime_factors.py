#  File:       prime_factors.py
#  Purpose:    Compute the prime factors of a given natural number.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Monday 26 September 2016, 12:05 AM


def prime_factors(number):
    factors = []
    if number > 1:
        for num in range(2, number):
            if (number % num) == 0:
                factors.append(num)
                return factors
                break
            else:
                return True
    else:
        return factors
