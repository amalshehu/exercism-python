#  File       :	twelve_days.py
#  Purpose    :	Write a program that outputs the lyrics to 'The Twelve Days '
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Saturday 8 October 2016, 06:45 PM
import inflect
gift = ["Drummers Drumming", 'Pipers Piping', 'Lords-a-Leaping',
        'Ladies Dancing', 'Maids-a-Milking', 'Swans-a-Swimming',
        'Geese-a-Laying', 'Gold Rings', 'Calling Birds', 'French Hens',
        'Turtle Doves', 'a Partridge in a Pear Tree.\n']
gift_key = [x for x in range(1, 13)]
gifts = dict(zip(gift_key, reversed(gift)))


def sing():
    return verses(1, 12)


def verse(v):
    p = inflect.engine()
    day = p.number_to_words(v)
    day_count = p.ordinal(day)
    if v == 1:
        lyric = "On the %s day of Christmas my true love gave" \
                "to me, " % (day_count)
        lyric = lyric + gifts[v]
        return lyric
    if v > 1:
        lyric = "On the %s day of Christmas my true love gave" \
                "to me, " % (day_count)
        for k in range(v, 1, -1):
            num = p.number_to_words(k)
            lyric = lyric + num + " " + gifts[k] + ", "
        lyric += "and " + gifts[1]
        return lyric


def verses(v1, v2):
    lyric = ''
    for i in range(v1, v2+1):
        lyric += verse(i) + '\n'
    return lyric

print (sing())
