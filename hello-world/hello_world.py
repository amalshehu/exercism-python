#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if not name == '':
        message = "Hello, " + name + "!"
        return message
    else:
        return "Hello, World!"
