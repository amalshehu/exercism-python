#  File       :	perfect_numbers.py
#  Purpose    :	The Greek mathematician Nicomachus devised a
#               classification scheme for natural numbers.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Sunday 2 October 2016, 09:04 PM

Abundant = False
Deficient = False


def is_perfect(num):
    factor = sum([n for n in range(1, num+1) if n % num == 0])
    if num == fact_sum:
        return True
    elif num > fact_sum:
        return Deficient
    elif num < fact_sum:
        return Abundant
