#  File:       etl.py
#  Purpose:    To do the `Transform` step of an Extract-Transform-Load.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 22 September 2016, 03:40 PM


def transform(num):
    old = {
           1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
           2: ["D", "G"],
           3: ["B", "C", "M", "P"],
           4: ["F", "H", "V", "W", "Y"],
           5: ["K"],
           8: ["J", "X"],
           10: ["Q", "Z"]
    }
    return old[num]

print(transform(1))
