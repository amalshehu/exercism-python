#  File:       sublist.py
#  Purpose:    Write a function to determine if a list is a
#              sublist of another list.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Wednesday 28 September 2016, 09:40 PM

SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def check(_list, sub_list):
    for i in range(len(_list) + 1 - len(sub_list)):
        if _list[i:i + len(sub_list)] == sub_list:
            return True


def check_lists(_list, sub_list):
    if len(_list) > len(sub_list):
        if check(_list, sub_list):
            return SUPERLIST

    if len(sub_list) > len(_list):
        if check(sub_list, _list):
            return SUBLIST
    if len(_list) == len(sub_list):
            return EQUAL if _list == sub_list else UNEQUAL
    return UNEQUAL
