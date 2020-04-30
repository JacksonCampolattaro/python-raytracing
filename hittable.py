from vec3 import Vec3


class HitRecord(object):
    def __init__(self):

        self.position = Vec3()
        self.normal = Vec3()

        self.t = 0.0
        self.frontFacing = False

    def setFaceNormal(self, ray, outwardNormal):
        self.frontFacing = ray.direction.dot(outwardNormal) < 0
        if self.frontFacing:
            self.normal = outwardNormal
        else:
            self.normal = -outwardNormal


class Hittable(object):
    def hit(self, ray, t_min, t_max):
        raise NotImplementedError()


class HittableList(Hittable):

    objects = []

    def hit(self, ray, t_min, t_max):

        hitAnything = False
        t_closest = t_max
        rec = HitRecord()

        for object in self.objects:

            hit, tempRec = object.hit(ray, t_min, t_closest)

            if hit:
                hitAnything = True
                t_closest = tempRec.t
                rec = tempRec

        return hitAnything, rec
