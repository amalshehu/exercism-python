#  File:       circular_buffer.py
#  Purpose:    A data structure that uses a single, fixed-size buffer
#              as if it were connected end-to-end.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 29 September 2016, 10:48 PM


class CircularBuffer(object):

    def __init__(self, size_max):
        self.max = bytearray(size_max)  # bytearray represents a mutable sequence of bytes.
        self.read_head, self.write_head = 0
        
