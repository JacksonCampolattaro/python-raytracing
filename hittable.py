from vec3 import Vec3


class HitRecord(object):

    position = Vec3()
    normal = Vec3()
    t = 0.0
    frontFacing = False

    def setFaceNormal(self, ray, outwardNormal):
        self.frontFacing = ray.direction.dot(outwardNormal) < 0
        if self.frontFacing:
            self.normal = outwardNormal
        else:
            self.normal = -outwardNormal


class Hittable(object):
    def hit(self, ray, t_min, t_max):
        raise NotImplementedError()
