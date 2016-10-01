#  File:       nth_prime.py
#  Purpose:    Write a program that can tell you what the nth prime is.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 30 September 2016, 11:50 PM


def nth_prime(limit):

    for num in range(limit):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print num

print nth_prime(15)
