#  File:       rna-transcription.py
#  Purpose:    Write a program that, given a DNA strand,
#              returns its RNA complement (per RNA transcription).
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 1st September 2016, 07:15 PM


def to_rna(dna):
    dna = list(dna)
    data = {"G": "C", "C": "G", "T": "A", "A": "U", "U": "A"}
    rna = []
    for d in dna:
        if d == d in data:
            rna.append(data[d])
    print("".join(str(x) for x in rna))

to_rna("GCTAU")
