# Leap year python


def leap(year):
    if (year % 400) == 0 or (year % 4) == 0 and (year % 100) != 0:
                return "leap Year"

    else:
                return "not a leap year"
