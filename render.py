from vec3 import Vec3
from camera import Camera

import random


def ray_color(ray, world, depth=0):

    if depth <= 0:
        return Vec3(0.0, 0.0, 0.0)

    hit, rec = world.hit(ray, 0.001, 100000)

    if hit:

        ret, scattered, attenuation = rec.material.scatter(ray, rec)

        if ret:
            return attenuation * ray_color(scattered, world, depth - 1)

        return Vec3(0.0, 0.0, 0.0)

    unit_direction = ray.direction.norm()
    t = 0.5 * (unit_direction.y + 1.0)
    return ((1.0 - t) * Vec3(1.0, 1.0, 1.0)) + (t * Vec3(0.5, 0.7, 1.0))


def sample(world, camera, j, i):

    u = (i + random.random()) / camera.image_width
    v = (j + random.random()) / camera.image_height

    ray = camera.getRay(u, v)

    return ray_color(ray, world, 10)


def pixel(world, camera, samples_per_pixel, j, i):

    color = Vec3(0.0, 0.0, 0.0)

    # with Pool() as pool:
    for _ in range(samples_per_pixel):

        color += sample(world, camera, j, i)

    color /= samples_per_pixel
    # pixels[i, image_height - j - 1] = tuple(color)
    return color
