#  File:       sieve.py
#  Purpose:    Write a program that uses the Sieve of Eratosthenes to find all the primes from 2 up to a given number.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 3rd September 2016, 09:15 PM


def prime(limit):
    num = []
    for x in range(2, limit+1):
        num.append(x)

    return num

print (prime(100))
