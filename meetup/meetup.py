#  File:       meetup.py
#  Purpose:    Calculate the date of meetups.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 11:20 PM

import calendar
from datetime import date

dayNames = [day for day in calendar.day_name]


def meetup_day(m_Year, m_Month, weekday, SPD):
    dayStart = dayNames.index(weekday)
    chanceDate = [
        weekItem[dayStart]
        for weekItem in calendar.monthcalendar(m_Year, m_Month)
        if weekItem[dayStart]]

    if SPD == 'teenth':
        for dayItem in chanceDate:
            if 13 <= dayItem <= 19:
                return date(m_Year, m_Month, dayItem)
    elif SPD == 'last':
        dayStart = -1
    elif SPD == 'first':
        dayStart = 0
    else:
        dayStart = int(SPD[0]) - 1
    return date(m_Year, m_Month, chanceDate[dayStart])
