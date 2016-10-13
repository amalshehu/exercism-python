#  File       :	binary.py
#  Purpose    :	Write a program that will convert a binary number, represented as a string (e.g. '101010'), to its decimal equivalent using first principles
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Saturday 12 October 2016, 03:02 PM

def parse_binary(bin_value):
    sum_ = 0
    for i in bin_value:
        sum_ = sum_ * 2 + int(i)
    return sum_
