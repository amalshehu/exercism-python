#  File:       pythagorean_triplet.py
#  Purpose:    A Pythagorean triplet program
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 29 September 2016, 04:30 PM


def pythagorean_triples(n):
    n = int(n)
    if n>0:
        if a in range(1,n-1):
            if b in range(a+1, n):
                if c in range(b+1,n+1):
                    if a*a+b*b==c*c:
                        print a,b,c
    else:
        return "Wrong input"

pythagorean_triples(30)
