#  File:       circular_buffer.py
#  Purpose:    A data structure that uses a single, fixed-size buffer
#              as if it were connected end-to-end.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Thursday 29 September 2016, 10:48 PM


class CircularBuffer(object):

    def __init__(self, size_max):
        self.maxBuffer = bytearray(size_max)  # bytearray represents a mutable sequence of bytes.
        self.readHead, self.writeHead = 0

    def insert_data(self, value):
        self.maxBuffer[self.writeHead] = value

    def clean(self):
        self.maxBuffer = bytearray(len(self.maxBuffer))

    def write(self, value):
        if all(self.maxBuffer):
            raise FullBufferException
        self.insert_data(value)
        self.writeHead = (self.writeHead + 1) % len(self.maxBuffer)
        
