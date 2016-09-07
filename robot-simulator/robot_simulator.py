#  File:       robot_simulator.py
#  Purpose:    A robot factory's test facility needs a program to verify robot movements.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 3rd September 2016, 05:00 PM

.class Robot(object):
    """docstring for Robot."""
    def __init__(self,movement, x, y):

        self.movement = movement
        self.x = x_axis = 0
        self.y = y_axis = 0

    def advance(Robot):
        x_axis += 1

    def advance_twice(Robot):
        x_axis += 2

    def left(Robot):
        x_axis -= 1

    def right(Robot):
        x_axis += 1

    def instruction(Robot, move):
        if move == "A":
            super advance(x_axis, y_axis)
        elif move == "AA":
            super advance_twice(x_axis, y_axis)

        elif move == "R":
            super right(x_axis, y_axis)

        elif move == "L":
            super left(x_axis, y_axis)

asimo = Robot
asimo.instruction(x, y)
