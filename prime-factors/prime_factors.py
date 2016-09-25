#  File:       prime_factors.py
#  Purpose:    Compute the prime factors of a given natural number.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Monday 26 September 2016, 12:05 AM


def prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return number % num
            else:
                return True
    else:
        return False
        
