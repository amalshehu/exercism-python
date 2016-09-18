#  File:       grains.py
#  Purpose:    Write a program that calculates the number of grains of wheat
#              on a chessboard given that the number on each square doubles.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Sunday 18 September 2016, 05:25 PM

square = [x for x in range(1, 65)]
grains = [2 ** x for x in range(0, 65)]
board = dict(zip(square, grains))


def on_square(num):
    for k, v in board.iteritems():
        if k == num:
            return v


def total_after(num):
    total = 0
    for key, value in board.iteritems():
        if key == num:
            total += value
    return total


print (total_after(10))
print(on_square(10))
