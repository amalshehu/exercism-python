#  File       :	binary.py
#  Purpose    :	Write a program that will convert a binary number, represented as a string (e.g. '101010'), to its decimal equivalent using first principles
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Saturday 12 October 2016, 03:02 PM
import re
def parse_binary(bin_value):
    sum_ = 0
    for i in bin_value:
        matches = re.match('[01]*$',bin_value)
        if not matches:
            print i
            raise ValueError('Not a valid binary number.')
        sum_ = sum_ * 2 + int(i)
    return sum_

print parse_binary('1011')
