from vec3 import Vec3
from ray import Ray


class Camera(object):

    lower_left_corner = Vec3([-2.0, -1.0, -1.0])
    horizontal = Vec3([4.0, 0.0, 0.0])
    vertical = Vec3([0.0, 2.0, 0.0])
    origin = Vec3([0.0, 0.0, 0.0])

    def getRay(self, u, v):
        return Ray(
            self.origin,
            self.lower_left_corner
            + u * self.horizontal
            + v * self.vertical
            - self.origin,
        )
