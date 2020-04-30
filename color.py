import numpy
import math


def clamp(value, minimum, maximum):
    result = value if value > minimum else minimum
    result = result if value < maximum else maximum
    return result


class Color(numpy.ndarray):
    def __new__(cls, input_array=(0.0, 0.0, 0.0)):
        obj = numpy.asarray(input_array).view(cls)
        return obj

    @property
    def r(self):
        return self[0]

    @property
    def g(self):
        return self[1]

    @property
    def b(self):
        return self[2]

    def __iter__(self):
        for x in numpy.nditer(self):
            yield int(255 * clamp(math.sqrt(x.item()), 0, 0.999))
