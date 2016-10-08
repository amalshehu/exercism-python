#  File       :	secret_handshake.py
#  Purpose    :	Write a program that will take a decimal number, and
#               convert it to the sequence of events for a secret handshake.
#  Programmer : Amal Shehu
#  Course     :	Exercism
#  Date       :	Monday 3 October 2016, 12:50 AM

actions = {1: 'wink',
           2: 'double blink',
           4: 'close your eyes',
           8: 'jump'
           }
rev_action = dict(zip(actions.values(), actions.keys()))


def handshake(num):
    if type(num) == str:
        try:
            num = int(num, 2)
        except ValueError:
            return []
    if num <= 0:
        return []
    secret = [actions[2**i] for i in range(4) if num & 2**i]
    if num & 2**4:
        secret = secret[::-1]
    return secret


def code(actions):
    num = 0
    encoded = [0]
    back = False
    for item in actions:
        if item in rev_action:
            action_code = rev_action[item]
            if action_code <= 8:
                num += action_code
                if action_code < max(encoded):
                    back = True
                encoded.append(action_code)
        else:
            return '0'
    if back:
        num += 16
    binary = str(bin(num))[2:]
    return binary
print (handshake(9))
print (code(['wink', 'double blink', 'jump']))
