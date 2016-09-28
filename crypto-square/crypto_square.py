#  File:       crypto_square.py
#  Purpose:    Implement the method for composing secret messages called a square code.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Tuesday 28 September 2016, 03:27 PM


def crypto(message):
    normalized = ''.join(i for i in message.lower() if i.isalpha())
    print (normalized)

crypto("If man was meant to stay on the ground, god would have given us roots.")
