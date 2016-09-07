#  File:       sieve.py
#  Purpose:    Write a program that uses the Sieve of Eratosthenes to find all the primes from 2 up to a given number.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 3rd September 2016, 09:15 PM


def sieve(limit):
    num_sq = []
    prime = set()
    for x in range(2, limit+1):
        if x not in prime:
            for y in range(x, limit+1, x):
                prime.add(y)
            num_sq.append(x)
    return num_sq
