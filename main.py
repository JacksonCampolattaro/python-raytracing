from vec3 import Vec3
from color import Color
from ray import Ray
from hittable import Hittable, HittableList
from sphere import Sphere
from camera import Camera

from PIL import Image
import random

from functools import partial
from multiprocessing import Pool


def ray_color(ray, world):

    hit, rec = world.hit(ray, 0.1, 1000)

    t = rec.t

    if hit:
        return 0.5 * (Color([1, 1, 1]) + rec.normal)

    unit_direction = ray.direction.norm()
    t = 0.5 * (unit_direction.y + 1.0)
    return ((1.0 - t) * Color([1.0, 1.0, 1.0])) + (t * Color([0.5, 0.7, 1.0]))


image_height = 100
image_width = 200
samples_per_pixel = 10

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

camera = Camera()

world = HittableList()
world.objects.append(Sphere([0, 0, -1], 0.5))
world.objects.append(Sphere([0, -100.5, -1], 100))


def drawPixel(j, i):

    color = Color([0.0, 0.0, 0.0])

    for _ in range(samples_per_pixel):

        u = (i + random.random()) / image_width
        v = (j + random.random()) / image_height

        ray = camera.getRay(u, v)

        color += ray_color(ray, world)

    color /= samples_per_pixel
    # pixels[i, image_height - j - 1] = tuple(color)
    return color


def drawRow(j):

    with Pool() as pool:

        func = partial(drawPixel, j)
        colors = pool.map(func, range(image_width - 1))

        for i in range(image_width - 1):
            pixels[i, image_height - j - 1] = tuple(colors[i])


for j in range(image_height - 1):
    drawRow(j)
    print("{} / {}".format(j + 1, image_height), end="\r")

img.show()
