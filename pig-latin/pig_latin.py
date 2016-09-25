#  File:       pig_latin.py
#  Purpose:    Implement a program that translates from English to Pig Latin
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Monday 26 September 2016, 12:40 AM


def translate(english):
    pyg = 'ay'
    if len(english) > 0 and english.isalpha():
        word = english.lower()
        first = word[0]
        new_word = word[1:len(new_word)] + first + pyg
        return new_word

    else:
        return False
