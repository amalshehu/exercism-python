#  File:       space_age.py
#  Purpose:    Write a program that, given an age in seconds, calculates
#              how old someone is in terms of a given planet's solar years.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 17 September 2016, 06:09 PM


class SpaceAge(object):
    """docstring for SpaceAge."""
    def __init__(self, _seconds):
        self._seconds = _seconds

    def on_earth(self):
        return round((self._seconds / 31557600), 2)

    def on_mercury(self):
        return round((self._seconds / 31557600) * 0.240846, 2)

obj = SpaceAge(1e6)
print (obj.on_earth())
print (obj.on_mercury())
