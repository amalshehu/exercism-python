#  File:       bob.py
#  Purpose:    Bob
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 05:45 PM


def hey(what):

    if what.isupper():
        return "Whoa, chill out!"

    if what.strip() == "":
        return ("Fine. Be that way!")

    if what.endswith('?'):
        return ("Sure.")

    if what.endswith(' ') and '?' in what:
        return ("Sure.")
    else:
        return ("Whatever.")
