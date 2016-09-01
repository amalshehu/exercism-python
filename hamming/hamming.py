#  File:       hamming.py
#  Purpose:    calculate the Hamming difference between two DNA strands.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 1st September 2016, 11:00 PM

# Implementation notes

'''The Hamming distance is only defined for sequences of equal length.
 This means that based on the definition, each language could deal with
 getting sequences of equal length differently.'''


def distance(dna1, dna2):
    hamm = 0
    for h1, h2 in zip(dna1, dna2):
        if h1 != h2:
            hamm += 1
    return hamm
