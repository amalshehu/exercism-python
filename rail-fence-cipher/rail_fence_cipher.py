#  File:       rail_fence_cipher.py
#  Purpose:    Implement encoding and decoding for the rail fence cipher.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 30 September 2016, 08:35 PM


class Rail():
    """Implementation of Rail Fence Cipher."""
    def __init__(self, text, rail_count):
        self.text = text
        self.rail_count = rail_count

    def imaginary_fence(self):
        fence = [[None] * len(self.text) for num in range(self.rail_count)]
        print (fence)

f = Rail('helloworld', 3)
f.imaginary_fence()
