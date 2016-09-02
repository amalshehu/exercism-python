#  File:       bob.py
#  Purpose:    Bob
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 05:45 PM


def hey(what):

    what = what.strip()

    if what.isupper():
        return "Whoa, chill out!"

    if what == "":
        return ("Fine. Be that way!")

    if what[-1] == '?' in what:
        return ("Sure.")
    else:
        return ("Whatever.")
