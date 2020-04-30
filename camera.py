from vec3 import Vec3
from ray import Ray
import math
import numpy


class Camera(object):
    def __init__(self, lookfrom, lookat, vup, vfov, aspect):

        theta = math.radians(vfov)
        half_height = math.tan(theta / 2.0)
        half_width = aspect * half_height

        w = (lookfrom - lookat).norm()
        u = Vec3(numpy.cross(vup, w)).norm()
        v = Vec3(numpy.cross(w, u))

        self.origin = lookfrom
        self.lower_left_corner = self.origin - half_width * u - half_height * v - w
        self.horizontal = 2 * half_width * u
        self.vertical = 2 * half_height * v

    def getRay(self, u, v):
        return Ray(
            self.origin,
            self.lower_left_corner
            + u * self.horizontal
            + v * self.vertical
            - self.origin,
        )
