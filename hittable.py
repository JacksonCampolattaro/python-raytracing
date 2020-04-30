from vec3 import Vec3


class HitRecord(object):
    t = 0.0
    position = Vec3()
    normal = Vec3()


class Hittable(object):
    def hit(self, ray, t_min, t_max):
        raise NotImplementedError()
