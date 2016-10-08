#  File       :	twelve_days.py
#  Purpose    :	Write a program that outputs the lyrics to 'The Twelve Days '
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Saturday 8 October 2016, 06:45 PM
import inflect
p = inflect.engine()
word_form = p.number_to_words(5)
ordinal_word = p.ordinal(word_form)
print (ordinal_word)

gifts = enumerate {"Drummers Drumming", 'Pipers Piping', 'Lords-a-Leaping',
         'Ladies Dancing', 'Maids-a-Milking','Swans-a-Swimming',
         'Geese-a-Laying','Gold Rings', 'Calling Birds',' French Hens',
         'Turtle Doves', 'Partridge'}
gifts.reverse()
print (gifts)

def sing():
    pass


def verse(v):
    pass


def verses(v1, v2):
    pass
