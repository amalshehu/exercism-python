#  File:       nth_prime.py
#  Purpose:    Write a program that can tell you what the nth prime is.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 30 September 2016, 11:50 PM


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
                if not num % i:
                    return False
        return True


def nth_prime(limit):
    prime = []
    for i in range(10000):
        if is_prime(i):
            prime.append(i)
        if len(prime) == limit:
            break
    print prime
    return prime[limit-1]
