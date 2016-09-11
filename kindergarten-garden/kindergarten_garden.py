#  File:       kindergarten_garden.py
#  Purpose:    Write a program that, given a diagram, can tell you which plants
#              each students in the kindergarten class is responsible for.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 10th September 2016, 10:51 PM


class Garden(object):
    child_names = ["Alice", "Bob", "Charlie", "David",
                   "Eve", "Fred", "Ginny", "Harriet",
                   "Ileana", "Joseph", "Kincaid", "Larry"]
    plant_names = {"C": "Clover", "G": "Grass",
                   "R": "Radishes", "V": "Violets"}

    def __init__(self, blueprint, students=child_names):
        self.students = sorted(students)
        self.cup_row = blueprint.split()

    def plants(self, students):
        cup_start = self.students.index(students) * 2
        cup = slice(cup_start, cup_start + 2)
        test_cup = (self.cup_row[0][cup] + self.cup_row[1][cup])
        plant = [self.plant_names[item] for item in test_cup]
        return plant

garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print (garden.plants("Alice"))
