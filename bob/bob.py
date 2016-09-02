#  File:       bob.py
#  Purpose:    Bob
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 05:45 PM


def hey(what):
    if what is None or what.strip() == " ":
        return ("Fine. Be that way")

    if what.endswith('?'):
        return ("Sure")

    if what.isupper() and what.isalnum:

        return "Whoa, chill out!"

    return ("Whatever")
