#  File:       matrix.py
#  Purpose:    Write a program that, given a string representing a matrix
#              of numbers, can return the rows and columns of that matrix.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 30 September 2016, 07:11 PM
import re


class Matrix():

    """Matrix row and column."""
    def __init__(self, matrix):
        self.matrix = matrix

    def matrix_row(self, matrix):
        return re.findall(r'\d+', matrix)

mat = Matrix("12254646")
print(mat.matrix_row())
