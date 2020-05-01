import numpy
import random
import math


# A simple 3d vector class
class Vec3(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, other):

        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return Vec3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):

        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):

        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):

        if isinstance(other, Vec3):
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            return Vec3(self.x / other, self.y / other, self.z / other)

    def length_squared(self):
        x = self.x
        y = self.y
        z = self.z
        return math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)

    def length(self):
        return math.sqrt(self.length_squared())

    def norm(self):
        return self / self.length()

    def dot(self, other):
        return dot(self, other)


def dot(u, v):
    return (u.x * v.x) + (u.y * v.y) + (u.z * v.z)


def cross(u, v):
    return Vec3(
        (u.y * v.z) - (u.z * v.y), (u.z * v.x) - (u.x * v.z), (u.x * v.y) - (u.y * v.x)
    )


def unit_vector(v):
    return v / v.length()


def random_in_unit_sphere():
    while True:
        p = Vec3().random(-1.0, 1.0)
        if p.length() <= 1:
            return p


def random_unit_vector():
    a = random.uniform(0, 2 * math.pi)
    z = random.uniform(-1.0, 1.0)
    r = math.sqrt(1 - z * z)
    return Vec3(r * math.cos(a), r * math.sin(a), z)


def random_in_hemisphere(normal):
    in_unit_sphere = random_in_unit_sphere()
    if in_unit_sphere.dot(normal):
        return in_unit_sphere
    else:
        return -in_unit_sphere


def reflect(vector, normal):
    return vector - 2 * vector.dot(normal) * normal


def refract(vector, normal, etai_over_etat):
    cos_theta = normal.dot(-vector)
    r_out_parallel = etai_over_etat * (vector + cos_theta * normal)
    r_out_perpendicular = (
        -math.sqrt(1.0 - r_out_parallel.length() * r_out_parallel.length()) * normal
    )
    return r_out_parallel + r_out_perpendicular
