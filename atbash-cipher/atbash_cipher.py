#  File:       atbash_cipher.py
#  Purpose:    Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 3rd September 2016, 09:15 PM


alpha = "abcdefghijklmnopqrstuvwxyz"
rev = list(alpha)[::-1]
store = dict(zip(alpha, rev))


def decode(string):
    dec = ''
    for x in string:
        dec += str(store[x])
    return dec


def encode(string):
    enc = ''
    for x in string:
        enc += str(store.keys[x])
    return enc
