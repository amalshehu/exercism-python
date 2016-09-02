#  File:       meetup.py
#  Purpose:    Calculate the date of meetups.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 11:20 PM

import calendar
from datetime import date


def meetup_day(m_Year, m_Month, weekDay, specWeekday):
    lastDay = calendar.monthrange(year, month)[1]
    print(lastDay)
    weekDay_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
