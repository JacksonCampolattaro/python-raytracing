from hittable import HitRecord
from vec3 import Vec3, random_unit_vector
from ray import Ray


class Material(object):
    def scatter(self, ray_in, rec):
        raise NotImplementedError()


class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, rec):

        scatter_direction = rec.normal + random_unit_vector()
        scattered = Ray(rec.position, scatter_direction)
        attenuation = self.albedo
        return scattered, attenuation
