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
reverse_actions = dict(zip(actions.values(), actions.keys()))
print(actions)
print (reverse_actions)


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
