import numpy
import math


def clamp(value, minimum, maximum):
    result = value if value > minimum else minimum
    result = result if value < maximum else maximum
    return result


class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __iter__(self):
        yield int(255 * clamp(math.sqrt(self.r), 0, 0.999))
        yield int(255 * clamp(math.sqrt(self.g), 0, 0.999))
        yield int(255 * clamp(math.sqrt(self.b), 0, 0.999))
