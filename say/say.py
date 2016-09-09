#  File:       say.py
#  Purpose:    0 to 999,999,999,999 and spell out that number in English.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Wednesday 8th September 2016, 10:00 PM

# #### Step 1


def say(num):
    num_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
          5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
          11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
          15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
          19: 'ninteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
          50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
          90: 'ninty'}

    if (num < 20):
        return num_dict[num]

    if (num < 100):
        if num % 10 == 0:
            return num_dict[num]
        else:
            return num_dict[num // 10 * 10] + '-' + num_dict[num % 10]
