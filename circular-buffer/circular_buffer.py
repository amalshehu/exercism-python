#  File:       circular_buffer.py
#  Purpose:    A data structure that uses a single, fixed-size buffer
#              as if it were connected end-to-end.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 29 September 2016, 10:48 PM

import collections


def CircularBuffer(value):
    d = collections.deque(maxlen=7)
    for i in xrange(10):
        d.append(i)
