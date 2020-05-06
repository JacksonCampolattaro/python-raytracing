from hittable import HitRecord
from vec3 import Vec3, random_in_unit_sphere, random_unit_vector, dot, refract, reflect
from ray import Ray
import random
import math


class Material(object):
    def scatter(self, ray_in, rec):
        raise NotImplementedError()


class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, rec):

        scatter_direction = random_unit_vector() + rec.normal
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


class Dialectric(Material):
    def __init__(self, refractive_index):
        self.refractive_index = refractive_index

    def scatter(self, ray_in, rec):
        attenuation = Vec3(1.0, 1.0, 1.0)
        if rec.frontFacing:
            etai_over_etat = 1 / self.refractive_index
        else:
            etai_over_etat = self.refractive_index

        unit_direction = ray_in.direction.norm()

        cos_theta = min(dot(rec.normal, -unit_direction), 1.0)
        sin_theta = math.sqrt(1.0 - cos_theta * cos_theta)

        if etai_over_etat * sin_theta > 1.0:
            reflected = reflect(unit_direction, rec.normal)
            scattered = Ray(rec.position, reflected)
            return True, scattered, attenuation

        reflection_probability = schlick(cos_theta, etai_over_etat)
        if random.random() < reflection_probability:
            reflected = reflect(unit_direction, rec.normal)
            scattered = Ray(rec.position, reflected)
            return True, scattered, attenuation

        refracted = refract(unit_direction, rec.normal, etai_over_etat)
        scattered = Ray(rec.position, refracted)
        return True, scattered, attenuation


def schlick(cosine, refractive_index):
    r0 = (1 - refractive_index) / (1 + refractive_index)
    r0 = r0 * r0
    return r0 + (1 - r0) * math.pow((1 - cosine), 5)
