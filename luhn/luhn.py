#  File:       luhn.py
#  Purpose:    Write a program that can take a number and determine whether
#              or not it is valid per the Luhn formula.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Sunday 18 September 2016, 09:55 PM


class Luhn(object):
    def __init__(self, card_number):
        self.card_number = card_number

    def addends(self):
        def luhn_function(x): return (2 * x - 9) if (x > 4) else (2 * x)
        prev_digits = [item for item in str(self.card_number)]

        return int(prev_digits)

cdn = Luhn(1212)
print (cdn.addends())
