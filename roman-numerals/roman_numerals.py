#  File:       roman_numerals.py
#  Purpose:    Function to convert from normal numbers to Roman Numerals.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 17 September 2016, 03:30 PM

numerals = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))


def roman_numerals(num):
    roman = []
    for number, numeral in numerals:
        swing = num // number
        roman.append(numeral * swing)
        num -= number * swing
    return ''.join(roman)
