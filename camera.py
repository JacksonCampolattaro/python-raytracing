from vec3 import Vec3, cross
from ray import Ray
import math
import numpy


class Camera(object):
    def __init__(self, lookfrom, lookat, vup, vfov, aspect):

        theta = math.radians(vfov)
        half_height = math.tan(theta / 2.0)
        half_width = aspect * half_height

        w = (lookfrom - lookat).norm()
        u = cross(vup, w).norm()
        v = cross(w, u)

        self.origin = lookfrom
        self.lower_left_corner = self.origin - (u * half_width) - (v * half_height) - w
        self.horizontal = u * half_width * 2
        self.vertical = v * half_height * 2

    def __str__(self):
        print("origin: {} corner: {}".format(self.origin, self.lower_left_corner))

    def getRay(self, u, v):
        return Ray(
            self.origin,
            (self.lower_left_corner + (self.horizontal * u) + (self.vertical * v))
            - self.origin,
        )
