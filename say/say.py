#  File:       say.py
#  Purpose:    0 to 999,999,999,999 and spell out that number in English.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Wednesday 8th September 2016, 10:00 PM


def say(num):
    num_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
          5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
          11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
          15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
          19: 'ninteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
          50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
          90: 'ninty'}

    tho = 1000
    mil = tho * 1000
    bil = mil * 1000
    tril = bil * 1000
    assert(0 <= num)  # Test that condition, and trigger an error if is false.

    if (num < 20):
        return num_dict[num]

    if (num < 100):
        if num % 10 == 0:
            return num_dict[num]
        else:
            return num_dict[num // 10 * 10] + '-' + num_dict[num % 10]
    if (num < tho):
        if num % 100 == 0:
            return num_dict[num // 100] + ' hundred'
        else:
            return num_dict[num // 100] + ' hundred and ' + say(num % 100)

    if (num < mil):
        if num % tho == 0:
            return say(num // tho) + ' thousand'
        else:
            return say(num // tho) + ' thousand ' + say(num % tho)

    if (num < bil):
        if (num % mil) == 0:
            return say(num // mil) + ' million'
    else:
        return say(num // mil) + ' million ' + say(num % mil)

    if (num < tril):
        if (num % bil) == 0:
            return say(num // bil) + ' billion'
        else:
            return say(num // bil) + ' billion ' + say(num % bil)

    if (num % tril == 0):
        return say(num // tril) + ' trillion'
    else:
        return say(num // tril) + ' trillion ' + say(num % tril)

    raise AssertionError('Out of range: %s' % str(num))

print (say(1234567))
