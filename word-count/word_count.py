#  File:       word_count.py
#  Purpose:    Write a program that given a phrase can count the occurrences of each word in that phrase.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 2nd September 2016, 10:15 AM


def word_count(words):
    word = words.split()
    w = set(word)
    for x in w:
        print (x, word.count(x))
word_count("olly olly in come free")
