import numpy


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

    def norm(self):
        return self / linalg.norm(self)

    def __eq__(self, other):
        return numpy.array_equal(self, other)

    def __ne__(self, other):
        return not numpy.array_equal(self, other)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __iter__(self):
        for x in numpy.nditer(self):
            yield x.item()