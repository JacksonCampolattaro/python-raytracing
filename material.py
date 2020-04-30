from hittable import HitRecord
from vec3 import Vec3, random_unit_vector, random_in_unit_sphere, reflect
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
        return True, scattered, attenuation


class Metal(Material):
    def __init__(self, albedo, fuzz):
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, ray_in, rec):
        reflected = reflect(ray_in.direction.norm(), rec.normal)
        scattered = Ray(rec.position, reflected + self.fuzz * random_in_unit_sphere())
        attenuation = self.albedo
        val = scattered.direction.dot(rec.normal) > 0
        return val, scattered, attenuation
