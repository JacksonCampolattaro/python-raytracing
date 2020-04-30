from vec3 import Vec3
from ray import Ray
import math


class Camera(object):
    def __init__(self, vfov, aspect):

        theta = math.radians(vfov)
        half_height = math.tan(theta / 2.0)
        half_width = aspect * half_height

        self.origin = Vec3([0.0, 0.0, 0.0])
        self.lower_left_corner = Vec3([-half_width, -half_height, -1.0])
        self.horizontal = Vec3([2.0 * half_width, 0.0, 0.0])
        self.vertical = Vec3([0.0, 2.0 * half_height, 0.0])

    def getRay(self, u, v):
        return Ray(
            self.origin,
            self.lower_left_corner
            + u * self.horizontal
            + v * self.vertical
            - self.origin,
        )
