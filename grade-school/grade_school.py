#  File:       grade_school.py
#  Purpose:    Write a small archiving program that stores students' names along with the grade that they are in.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Monday 12th September 2016, 11:00 PM

from collections import defaultdict


class School(object):
    """docstring for School."""
    def __init__(self, name):
        self.name = name
        self.data = defaultdict(set)

    def add(self, student, grade):
        self.data[grade].add(student)
    def grade(self, stage):
        return self.data[stage]

    def sort(self):
        return sorted((grade, tuple(sorted(students)))
                      for grade, students in self.data.items())
