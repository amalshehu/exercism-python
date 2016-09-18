#  File:       luhn.py
#  Purpose:    Write a program that can take a number and determine whether
#              or not it is valid per the Luhn formula.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Sunday 18 September 2016, 09:55 PM


def Luhn(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd = digits[-1::-2]
    even = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
def checksum(card_number):
    return luhn(card_number)
