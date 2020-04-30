import numpy
import random
import math


# A simple 3d vector class
class Vec3(numpy.ndarray):
    def __new__(cls, input_array=(0, 0, 0)):
        obj = numpy.asarray(input_array).view(cls)
        return obj

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        return self[2]

    def dist(self, other):
        return numpy.linalg.norm(self - other)

    def length(self):
        return numpy.linalg.norm(self)

    def norm(self):
        return self / numpy.linalg.norm(self)

    def random(self, minimum, maximum):
        self = Vec3(
            [
                random.uniform(minimum, maximum),
                random.uniform(minimum, maximum),
                random.uniform(minimum, maximum),
            ]
        )
        return self

    def __eq__(self, other):
        return numpy.array_equal(self, other)

    def __ne__(self, other):
        return not numpy.array_equal(self, other)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __iter__(self):
        for x in numpy.nditer(self):
            yield x.item()


def random_in_hemisphere(normal):
    in_unit_sphere = random_in_unit_sphere()
    if in_unit_sphere.dot(normal):
        return in_unit_sphere
    else:
        return -in_unit_sphere


def random_in_unit_sphere():
    while True:
        p = Vec3().random(-1.0, 1.0)
        if p.length() <= 1:
            return p
