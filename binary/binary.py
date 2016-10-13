#  File       :	binary.py
#  Purpose    :	Write a program that will convert a binary number
#               to its decimal equivalent using first principles.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Saturday 12 October 2016, 03:02 PM
import re


def parse_binary(bin_value):
    sum_ = 0
    matches = re.match('[01]*$', bin_value)
    for i in bin_value:
        if not matches:
            raise ValueError('Not a valid binary number.')
        sum_ = sum_ * 2 + int(i)
    return sum_
