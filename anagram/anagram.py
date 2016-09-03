#  File:       anagram.py
#  Purpose:    Anagram
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 3rd September 2016, 02:45 PM


def detect_anagrams(string_1, string_2):
    str1List = list(string_1)
    str1List = [element.lower() for element in str1List]
    str1List.sort()
    str2List = list(string_2)
    str2List = [element.upper() for element in str2List]
    str2List.sort()

    return (str1List == str2List)
