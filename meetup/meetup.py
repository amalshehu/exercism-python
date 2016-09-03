#  File:       meetup.py
#  Purpose:    Calculate the date of meetups.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 2nd September 2016, 11:20 PM

import calendar
from datetime import date

dayNames = [day for day in calendar.day_name]


def meetup_day(m_Year, m_Month, weekDay, specWeekday):
    dayIndex =  dayNames.index(weekDay)
    chanceDate = [week[dayIndex]]
    for week in calendar.monthcalendar(m_Year, m_Month)
    if week[dayIndex]]

    if specWeekday == 'teenth':
        for dayNum in chanceDate:
            if 13<= dayNum <= 19:
                return date(m_Year, m_Month, dayNum)
