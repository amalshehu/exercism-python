#  File:       acronym.py
#  Purpose:    Convert a long phrase to its acronym
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Wednesday 7th September 2016, 11:50 PM


def abbreviate(words):
    out = ""
    for word in words.upper().split():
        out += (word[0])
    print (out)
