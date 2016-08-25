# Leap year python


def leap(year):
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
                return "leap Year"

    else:
                return "not a leap year"
