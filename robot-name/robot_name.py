#  File:       robot_name.py
#  Purpose:    Write a program that manages robot factory settings.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 30 September 2016, 03:00 PM

import string
import random


class Robot():
    """Robot facory settings"""
    def __init__(self):
        self.name = self.factory_name()

    def factory_name(self):
        char = ''.join(random.SystemRandom().choice(string.ascii_uppercase)
                       for _ in range(2))
        num = ''.join(random.SystemRandom().choice(string.digits)
                      for _ in range(3))
        robo = char + num
        return robo

    def reset(self):
        self.name = self.factory_name()

R1 = Robot()
print(R1.factory_name())
