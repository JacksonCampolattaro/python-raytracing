from hittable import Hittable, HitRecord
from vec3 import Vec3
import math


class Sphere(Hittable):

    center = Vec3()
    radius = 1.0

    def __init__(self, center, radius):

        self.center = center
        self.radius = radius

    def hit(self, ray, t_min, t_max):

        oc = ray.origin - self.center
        a = ray.direction.length() * ray.direction.length()
        half_b = oc.dot(ray.direction)
        c = (oc.length() * oc.length()) - (self.radius * self.radius)
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
                return True, rec

            temp = (-half_b + root) / a
            if t_min < temp < t_max:
                rec = HitRecord()
                rec.t = temp
                rec.position = ray.at(rec.t)
                outwardNormal = (rec.position - self.center) / self.radius
                rec.setFaceNormal(ray, outwardNormal)
                return True, rec

        return False, HitRecord()
