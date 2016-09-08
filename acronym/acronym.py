#  File:       acronym.py
#  Purpose:    Convert a long phrase to its acronym
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Wednesday 7th September 2016, 11:50 PM
import re


def abbreviate(words):
    out = []
    for word in re.findall(r"[A-Z]+[a-z]*|[a-z]+", words):
        out.append(word[0].upper())
    return "".join(out)

print (abbreviate("HyperText Markup Language"))
