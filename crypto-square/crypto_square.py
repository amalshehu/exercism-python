#  File:       crypto_square.py
#  Purpose:    Implement the method for composing secret messages called a square code.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Tuesday 28 September 2016, 03:27 PM


def normalize(message):
    return ''.join(i for i in message.lower() if i.isalpha())

def text_square(text, num):
    if len(text) <= num:
        return [text]
    return [text[:num]] + text_square(text[num:], num)

    
