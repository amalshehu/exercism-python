#  File:       grains.py
#  Purpose:    Write a program that calculates the number of grains of wheat
#              on a chessboard given that the number on each square doubles.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Sunday 18 September 2016, 05:25 PM
import itertools


square = [x for x in range(1, 65)]
grains = [2 ** x for x in range(0, 65)]
board = dict(zip(square, grains))


def on_square(num):
    for k, v in board.iteritems():
        if k == num:
            return v


def total_after(num):
    for k, v in board.iteritems():
        if k == num:
            total_after = sum(map(board.get, itertools.takewhile(lambda key: key != v, board)))
    return total_after

print (board)
print (total_after(1))
print(on_square(1))
