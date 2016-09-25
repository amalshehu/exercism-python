#  File:       prime_factors.py
#  Purpose:    Compute the prime factors of a given natural number.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Monday 26 September 2016, 12:05 AM


def prime_factors(number):
        num = 2
        factors = []
        while num <= number:
            if (number % num) == 0:
                number /= num
                factors.append(num)
            else:
                num += 1

        return factors
