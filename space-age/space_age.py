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
        planet = self.on_earth() * 0.2408467
        return planet

    def on_venus(self):
        planet = self.on_earth() * 0.61519726
        return planet
    def on_mars(self):
        planet = self.on_earth() * 1.8808158
        return planet

    def on_jupiter(self):
        planet = self.on_earth() * 11.862615
        return planet

    def on_saturn(self):
        planet = self.on_earth() * 29.447498
        return planet

    def on_uranus(self):
        planet = self.on_earth() * 84.016846
        return planet

    def on_neptune(self):
        planet = self.on_earth() * 164.79132
        return planet


obj = SpaceAge(1e6)
print (obj.on_earth())
print (obj.on_mercury())
