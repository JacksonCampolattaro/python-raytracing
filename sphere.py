from hittable import Hittable, HitRecord
from vec3 import Vec3, dot
import math


class Sphere(Hittable):
    def __init__(self, center, radius, material):

        self.center = center
        self.radius = radius
        self.material = material

    def hit(self, ray, t_min, t_max):

        oc = ray.origin - self.center
        a = ray.direction.length_squared()
        half_b = dot(oc, ray.direction)
        c = oc.length_squared() - (self.radius * self.radius)
        discriminant = (half_b * half_b) - (a * c)

        if discriminant > 0:

            root = math.sqrt(discriminant)

            temp = (-half_b - root) / a
            if t_min < temp < t_max:
                rec = HitRecord()
                rec.t = temp
                rec.position = ray.at(rec.t)
                outwardNormal = (rec.position - self.center) / self.radius
                rec.setFaceNormal(ray, outwardNormal)
                rec.material = self.material
                return True, rec

            temp = (-half_b + root) / a
            if t_min < temp < t_max:
                rec = HitRecord()
                rec.t = temp
                rec.position = ray.at(rec.t)
                outwardNormal = (rec.position - self.center) / self.radius
                rec.setFaceNormal(ray, outwardNormal)
                rec.material = self.material
                return True, rec

        return False, HitRecord()
