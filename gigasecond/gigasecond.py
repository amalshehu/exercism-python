#  File:       gigasecond.py
#  Purpose:    Calculate date that someone will celebrate their 1Gsanniversary.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 05:00 PM

from datetime import timedelta, datetime


def add_gigasecond(date):

# A timedelta object represents a duration, the difference between two dates or times.
    delta = timedelta(seconds=10**9)
    print (date + delta)

add_gigasecond(datetime(2016, 9, 2))
