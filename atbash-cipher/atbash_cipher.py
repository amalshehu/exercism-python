#  File:       atbash_cipher.py
#  Purpose:    Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 3rd September 2016, 09:15 PM


def atbash_cipher(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rev = list(alpha)[::-1]
    store = dict(zip(alpha, rev))
    print (store)



atbash_cipher("abcd")
