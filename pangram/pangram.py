#  File:       pangram.py
#  Purpose:     # Determine if a sentence is a pangram.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 1st September 2016, 02:15 PM

'''
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
"every letter") is a sentence using every letter of the alphabet at least once.
The best known English pangram is "The quick brown fox jumps over the
lazy dog."The alphabet used is ASCII, and case insensitive, from 'a' to 'z'
inclusively.
'''



def pangram(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    storeStr = ""
    for x in string:
        if x in alpha:
            storeStr += x
    for x in alpha:
        if x not in string:
            print (storeStr, alpha)
            return False

    return True
