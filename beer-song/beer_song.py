#  File       :	beer_song.py
#  Purpose    :	Write a program which produces the lyrics to that beloved
#               classic, that field-trip : 99 Bottles of Beer on the Wall.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Sunday 2 October 2016, 01:33 AM


def beer_song():
    for beer_count in range(99, 0, -1):
        if beer_count > 1:
            print beer_count, "bottles of beer on the wall,", beer_count, "bottles of beer."
            if beer_count > 2:
                suffix = str(beer_count - 1) + " bottles of beer on the wall."
            else:
                suffix = "1 bottle of beer on the wall."
        elif beer_count == 1:
            print "1 bottle of beer on the wall, 1 bottle of beer."
            suffix = "no more beer on the wall!"
            print "Take one down, pass it around,", suffix
            print "--"

beer_song()
