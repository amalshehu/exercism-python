#  File       :	beer_song.py
#  Purpose    :	Write a program which produces the lyrics to that beloved
#               classic, that field-trip : 99 Bottles of Beer on the Wall.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Sunday 2 October 2016, 01:33 AM


def song():
    for beer_count in range(99, -1, -1):
        verse(beer_count)


def verse(beer_count):
    if beer_count > 1:
        print beer_count, "bottles of beer on the wall,", beer_count, "bottles of beer.\n"
        current_count = beer_count - 1
        print "Take one down and pass it around,", current_count, "bottles of beer on the wall.\n"
        if beer_count > 2:
            suffix = str(beer_count - 1) + " bottles of beer on the wall.\n"
        else:
            suffix = "1 bottle of beer on the wall.\n"
    elif beer_count == 1:
        print "1 bottle of beer on the wall, 1 bottle of beer.\n"
        suffix = "no more beer on the wall!\n"
        print "Take one down, pass it around,", suffix

    elif beer_count == 0:
        print "No more bottles of beer on the wall, no more bottles of beer.\n"
        print "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
