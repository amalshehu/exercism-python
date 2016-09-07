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

    """docstring for Robot."""
    def __init__(self, front = NORTH, x_axis = 0, y_axis = 0):

        self.counterpart = (x_axis, y_axis)
        self.front = front

    def advance(self):
        x_axis, y_axis = self.counterpart[0], self.counterpart[1]
        if self.front == NORTH:
            self.counterpart = x_axis, y_axis+1
        elif self.front == EAST:
            self.counterpart = x_axis+1, y_axis
        elif self.front == SOUTH:
            self.counterpart = x_axis, y_axis-1
        elif self.front == WEST:
            self.counterpart = x_axis-1,y_axis

    def left(self):
        self.front = (self.front-1) % 4

    def right(self):
        self.front = (self.front + 1) % 4

    def simulate(self, move):
        for i in move:
    		if i == 'R':
    			self.right()
    		elif i == 'L':
    			self.left()
    		elif i == 'A':
    			self.advance()
