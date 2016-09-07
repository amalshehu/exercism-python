#  File:       robot_simulator.py
#  Purpose:    A robot factory's test facility needs a program to verify robot movements.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 3rd September 2016, 05:00 PM

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:

    """docstring for Robot simulator."""
    def __init__(self, bearing=NORTH, x_axis=0, y_axis=0):

        self.coordinates = (x_axis, y_axis)
        self.bearing = bearing

    def advance(self):
        x_axis, y_axis = self.coordinates[0], self.coordinates[1]
        if self.bearing == NORTH:
            self.coordinates = x_axis, y_axis+1
        elif self.bearing == EAST:
            self.coordinates = x_axis+1, y_axis
        elif self.bearing == SOUTH:
            self.coordinates = x_axis, y_axis-1
        elif self.bearing == WEST:
            self.coordinates = x_axis-1, y_axis

    def turn_left(self):
        self.bearing = (self.bearing-1) % 4

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def simulate(self, move):
        for i in move:
            if i == 'R':
                self.turn_right()
            elif i == 'L':
                self.turn_left()
            elif i == 'A':
                self.advance()
