#  File:       clock.py
#  Purpose:     # Clock
'''Implement a clock that handles times without dates.
   Create a clock that is independent of date.
   You should be able to add and subtract minutes to it.
   Two clocks that represent the same time should be equal to each other.'''
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 1st September 2016, 10:30 AM


class Clock(object):
    """docstring for Clock."""
    objectz = []

    def __new__(clk, hour, minute):
        for obj in objectz:
            if clk.objectz == obj:
                return obj
        return clk._obj_Inst

    def __init__(self, hour, minute):

        self.hour = (hour + (minute / 60)) % 24
        self.minute = minute % 60

    def __eq__(self, another):
        return self.hour == another.minute and self.minute == another.minute

    def __str__(self):
        return "{0:0d}:{1:0d}".format(self.hour,self.minute)

    def add(self, minute_x):
        return Clock(self.hour,self.minute + minute_x)
