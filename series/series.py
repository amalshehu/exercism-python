#  File:       series.py
#  Purpose:    Write a program that will take a string of digits and give you
#              all the contiguous substrings of length `n` in that string.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 3rd September 2016, 10:50 PM


def series(number, sub_len):
    num_list = [x for x in number]

    for i in range(1, len(num_list)):


        print (i)


series(2345, 2)
