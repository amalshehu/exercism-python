#  File:       anagram.py
#  Purpose:    Anagram
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 3rd September 2016, 02:45 PM


def detect_anagrams(string_1, string_2):
    string_sort = sorted(string_1.lower())
    gram_list = []
    for item in string_2:
        if sorted(item.lower()) == string_sort and item.lower() != string_1.lower():
            gram_list.append(item)

    return gram_list
