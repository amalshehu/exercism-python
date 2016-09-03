#  File:       series.py
#  Purpose:    Write a program that will take a string of digits and give you
#              all the contiguous substrings of length `n` in that string.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 3rd September 2016, 10:50 PM


def slices(number, leng):
    numbers = [int(item) for item in number]
    if not 1 <= leng <= len(numbers):
        raise ValueError(" Slice length Error : " + str(leng))
    return [numbers[i:i + leng] for i in range(len(numbers) - leng + 1)]
