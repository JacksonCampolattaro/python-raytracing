from vec3 import Vec3, random_in_unit_sphere
from color import Color
from ray import Ray
from hittable import Hittable, HittableList
from sphere import Sphere
from camera import Camera

from PIL import Image
import random

from functools import partial
from multiprocessing import Pool


def ray_color(ray, world, depth=0):

    if depth <= 0:
        return Color([0.0, 0.0, 0.0])

    hit, rec = world.hit(ray, 0.1, 1000)

    if hit:
        target = rec.position + rec.normal + random_in_unit_sphere()
        return 0.5 * ray_color(
            Ray(rec.position, target - rec.position), world, depth - 1
        )

    unit_direction = ray.direction.norm()
    t = 0.5 * (unit_direction.y + 1.0)
    return ((1.0 - t) * Color([1.0, 1.0, 1.0])) + (t * Color([0.5, 0.7, 1.0]))


image_height = 100
image_width = 200
samples_per_pixel = 10
max_depth = 50

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

camera = Camera()

world = HittableList()
world.objects.append(Sphere([0, 0, -1], 0.5))
world.objects.append(Sphere([0, -100.5, -1], 100))


def sample(j, i):

    u = (i + random.random()) / image_width
    v = (j + random.random()) / image_height

    ray = camera.getRay(u, v)

    return ray_color(ray, world, max_depth)


def drawPixel(j, i):

    color = Color([0.0, 0.0, 0.0])

    # with Pool() as pool:
    for _ in range(samples_per_pixel):

        color += sample(j, i)

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
