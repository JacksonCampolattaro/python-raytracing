from vec3 import Vec3


class Ray(object):

    origin = Vec3([0, 0, 0])
    direction = Vec3([0, 0, 0])

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return self.origin + t * self.direction
