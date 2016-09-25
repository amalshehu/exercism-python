#  File:       etl.py
#  Purpose:    To do the `Transform` step of an Extract-Transform-Load.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 22 September 2016, 03:40 PM


def transform(words):
    new_words = dict()
    for point, letters in words.items():
        for letter in letters:
            new_words[letter.lower()] = point
    return new_words
