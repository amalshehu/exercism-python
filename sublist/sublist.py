#  File:       sublist.py
#  Purpose:    Write a function to determine if a list is a sublist of another list.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Wednesday 28 September 2016, 09:40 PM
UNEQUAL = 0
EQUAL = 1
SUBLIST = 3
SUPERLIST = 4


def check_lists(_list, sub_list):
    for item in sub_list:
        if sub_list.count(item) == _list.count(item):
            return EQUAL
        elif sub_list.count(item) < _list.count(item):
            return SUBLIST
        elif sub_list.count(item) > _list.count(item):
            return SUPERLIST
        elif sub_list.count(item) != _list.count(item):
            return UNEQUAL
