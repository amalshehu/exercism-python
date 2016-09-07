#  File:       sum_of_multiples.py
#  Purpose:    Write a program that, given a number, can find the sum of all
#              the multiples of particular numbers up to but not including that number.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Wednesday 7th September 2016, 11:00 PM


def sum_of_multiples(limit, div_list):
    return sum(set(j for i in div_list if i > 0 for j in range(i, limit, i)))
