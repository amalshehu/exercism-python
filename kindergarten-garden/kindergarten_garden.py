#  File:       kindergarten_garden.py
#  Purpose:    Write a program that, given a diagram, can tell you which plants each child in the kindergarten class is responsible for.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 10th September 2016, 10:51 PM


class Garden(object):
    plant_names = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}
    def __init__(self, blueprint, child):
         self.child = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry"
         self.child = sorted(child.split())
         self.cup_row = blueprint.split()
    def plant(self, child):
        self.cup_start = self.child.index(child) * 2
        cup = slice(cup_start,cup_start + 2)
        for item in (cup_row[0][cup] + cup_row[1][cup])
        return self.plant_names[item]
