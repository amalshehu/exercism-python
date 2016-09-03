#  File:       anagram.py
#  Purpose:    Anagram
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 3rd September 2016, 02:45 PM


def detect_anagrams(str_1, string_2):
    str_sort = sorted(str_1.lower())
    gram_list = []
    for item in string_2:
        if sorted(item.lower()) == str_sort and item.lower() != str_1.lower():
            gram_list.append(item)

    return gram_list
