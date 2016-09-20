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
        def luhn_function(num): return (2 * num - 9) if (num > 4) else (2 * num)
        prev_digits = [int(item) for item in str(self.card_number)]
        for index, num in enumerate(prev_digits, start=len(prev_digits) % 2):
            if (index % 2 == 0):
                return luhn_function(num)
            else:
                return num

        def checksum(self):
            return sum(self.addends())

        def is_valid(self):
            return self.checksum() % 10 == 0

        @staticmethod
        def create(num):
            chk = (10 - Luhn(num * 10).checksum()) % 10
            return 10 * num + chk
