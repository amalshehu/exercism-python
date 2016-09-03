#  File:       difference_of_squares.py
#  Purpose:    To find th difference of squares of first n numbers
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 3rd September 2016, 01:50 PM


def sum_of_squares(number):
    return sum([i**2 for i in range(1, number+1)])


def square_of_sum(number):
    return sum(range(1, number+1)) ** 2


def difference(number):
    return square_of_sum(number) - sum_of_squares(number)
