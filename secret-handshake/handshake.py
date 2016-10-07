#  File       :	handshake.py
#  Purpose    :	Write a program that will take a decimal number, and
#               convert it to the sequence of events for a secret handshake.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Monday 3 October 2016, 12:50 AM


def handshake(num):
    return num


def converter(num):
    if num == 0:
        return ''
    else:
        return converter(num/2) + str(num % 2)
