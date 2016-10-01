#  File:	   saddle_points.py
#  Purpose:	Write a program that detects saddle points in a matrix.
#  Programmer: Amal Shehu
#  Course:	 Exercism
#  Date:	   Saturday 1 October 2016, 09:40 PM

def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Invalid Matrix Dimension")
    rows = matrix
    cols = zip(*matrix)
    point = set()
    for c in range(len(cols)):
        for r in range(len(rows)):
            saddle = matrix[r][c]
            if saddle == max(rows[r]) and saddle == min(cols[c]):
                point.add((r, c))
    return point
