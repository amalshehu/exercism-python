#  File:       pangram.py
#  Purpose:     # Determine if a sentence is a pangram.
'''
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
"every letter") is a sentence using every letter of the alphabet at least once.
The best known English pangram is "The quick brown fox jumps over the lazy dog."
The alphabet used is ASCII, and case insensitive, from 'a' to 'z'
inclusively.
'''
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 1st September 2016, 10:30 AM


def pangram(string):
    alpha = []
    for i in range(ord('a'), ord('n')+1):
        alpha.append((chr(i)))
    string = string.lower()
    print (string)


pangram("HelloWorld")
