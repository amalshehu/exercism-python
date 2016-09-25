#  File:       etl.py
#  Purpose:    To do the `Transform` step of an Extract-Transform-Load.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 22 September 2016, 03:40 PM


def transform(words):
    letters = dict(words)
    for letter in letters.iteritem():
        return letter.lower()
