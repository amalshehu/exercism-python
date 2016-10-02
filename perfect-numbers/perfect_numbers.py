#  File       :	perfect_numbers.py
#  Purpose    :	The Greek mathematician Nicomachus devised a
#               classification scheme for natural numbers.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Sunday 2 October 2016, 09:04 PM
from numpy import prod


def is_perfect(num):
    factor = []
    for n in range(1, num):
        if num % n == 0:
            factor.append(n)
    fact_sum = (sum(factor))
    fact_pro = prod(factor)
    if fact_pro == fact_sum:
        return True
    elif fact_pro > fact_sum:
        return False
    elif fact_pro < fact_sum:
        return False
