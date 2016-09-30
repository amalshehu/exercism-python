#  File:       matrix.py
#  Purpose:    Write a program that, given a string representing a matrix
#              of numbers, can return the rows and columns of that matrix.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 30 September 2016, 07:11 PM


class Matrix():

    """Matrix row and column."""
    def __init__(self, matrix):
        self.rows = self.matrix_row(matrix)
        self.columns = map(list, zip(*self.rows))

    def matrix_row(self, matrix):
        return [[int(i) for i in mat.split()] for mat in matrix.split('\n')]
