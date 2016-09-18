#  File:       grains.py
#  Purpose:    Write a program that calculates the number of grains of wheat
#              on a chessboard given that the number on each square doubles.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Sunday 18 September 2016, 05:25 PM

board = [x for x in range(1, 65)]
grains = [x*2 for x in range(1, 65)]

def on_square():
    for x in range(1, 65):
        board.append(x)
