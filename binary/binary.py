#  File       :	binary.py
#  Purpose    :	Write a program that will convert a binary number, represented as a string (e.g. '101010'), to its decimal equivalent using first principles
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Saturday 12 October 2016, 03:02 PM

def binary(bin_value):
    sum_ = 0
    num = list(bin_value)
    l = len(bin_value - 1)
    for i in num:
        sum_ += int(i) * (2 ** l)
    return sum_

print binary('11011')
