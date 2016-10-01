#  File:       rail_fence_cipher.py
#  Purpose:    Implement encoding and decoding for the rail fence cipher.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Friday 30 September 2016, 08:35 PM


class RailFence():
    """Implementation of Rail Fence Cipher."""
    def __init__(self, text, rail_count):
        self.text = text
        self.rail_count = rail_count
    def imaginary_fence(self, text, rail_count):
        fence = [[None] * len(self.text) for num in range(self.rail_count)]
        rails = range(self.rail_count - 1) + range(self.rail_count - 1, 0, -1)
        for n, letter in enumerate(self.text):
            fence[rails[n % len(rails)]][n] = letter
        if 0: # debug
            for rails in fence:
                print ''.join('.' if c is None else str(c) for c in rails)
        return [i for rail in fence for i in rail if i is not None]

    def encode(self):
        return ''.join(self.imaginary_fence(self.text, self.rail_count))

    def decode(self):
        r = range(len(self.text))
        dec = self.imaginary_fence(r, self.rail_count)
        return ''.join(self.text[dec.index(self.rail_count)] for self.rail_count in r)


rail = RailFence('WECRLTEERDSOEEFEAOCAIVDEN', 3)
print (rail.decode())
