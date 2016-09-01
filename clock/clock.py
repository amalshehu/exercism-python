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

    def __init__(self, arg):
        super(Clock, self).__init__()
        self.arg = arg
