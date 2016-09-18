#  File:       grains.py
#  Purpose:    Write a program that calculates the number of grains of wheat
#              on a chessboard given that the number on each square doubles.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Sunday 18 September 2016, 05:25 PM

square = [x for x in range(1, 65)]
grains = [2 ** x for x in range(0, 65)]

board = zip(square, grains)
print (board)
