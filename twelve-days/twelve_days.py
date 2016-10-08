#  File       :	twelve_days.py
#  Purpose    :	Write a program that outputs the lyrics to 'The Twelve Days '
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Saturday 8 October 2016, 06:45 PM
import inflect
p = inflect.engine()
word_form = p.number_to_words(5)
ordinal_word = p.ordinal(word_form)

gift = ["Drummers Drumming", 'Pipers Piping', 'Lords-a-Leaping',
        'adies Dancing', 'Maids-a-Milking','Swans-a-Swimming',
        'Geese-a-Laying','Gold Rings', 'Calling Birds',' French Hens',
        'Turtle Doves', 'Partridge']
gift_key = [x for x in range(1, 13)]
gifts = dict(zip(gift_key, reversed(gift)))

def sing():
    pass


def verse(v):
    p = inflect.engine()
    day = p.number_to_words(v)
    day_count = p.ordinal(day)
    if v <= 1:
            print "On the %s day of Christmas my true love gave to me, \
a %s in a Pear Tree." % (day_count, gifts[v])
    if v > 1:
        print "On the %s day of Christmas my true love gave to me, \
a %s in a Pear Tree." % (day_count, gifts[v])

def verses(v1, v2):
    pass

verse(2)
