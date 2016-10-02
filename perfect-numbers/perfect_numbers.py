#  File       :	perfect_numbers.py
#  Purpose    :	The Greek mathematician Nicomachus devised a
#               classification scheme for natural numbers.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Sunday 2 October 2016, 09:04 PM


def factors(num):
    factor = []
    for n in range(1, num):
        if num % n == 0:
            factor.append(n)
    return factor

print factors(5)
