#  File       :	handshake.py
#  Purpose    :	Write a program that will take a decimal number, and
#               convert it to the sequence of events for a secret handshake.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Monday 3 October 2016, 12:50 AM


def handshake(num):
    if len(converter(num)) > 6:
        raise AssertionError


    return num


def converter(num):
    if num == 0:
        return ''
    else:
        return converter(num/2) + str(num % 2)


def bin_converter(inp):
    r = 0
    for character in inp:
        if character == '0':
            r = r * 2
        elif character == '1':
            r = r * 2 + 1
        else:
            raise BinaryError()
    return r

print (bin_converter('1000'))
