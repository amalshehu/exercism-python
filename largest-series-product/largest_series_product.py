#  File:       largest_series_product.py
#  Purpose:    Calculate the largest product for a contiguous substring of digits of length n.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 9th September 2016, 08:02 PM

import re


def largest_product(num, size):
    multi = [reduce(lambda x, y: x * y, i, 1) for i in num_filter(num, size)]
    return max(multi)


def num_filter(num, size):
    if len(num) > size or num == re.match(r'^[0-9]*$'), num):
        raise ValueError
    return single(map(int, list(num)), size)


def single(x, size):
    return [x[i: i + size] for i in range(len(x) - size + 1)]
