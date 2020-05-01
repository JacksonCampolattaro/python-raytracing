from vec3 import Vec3
from color import Color
from hittable import HittableList
from sphere import Sphere
from camera import Camera
from material import Lambertian, Metal, Dialectric

from PIL import Image
import random


def ray_color(ray, world, depth=0):

    if depth <= 0:
        return Color([0.0, 0.0, 0.0])

    hit, rec = world.hit(ray, 0.001, 100000)

    if hit:

        ret, scattered, attenuation = rec.material.scatter(ray, rec)

        if ret:
            return attenuation * ray_color(scattered, world, depth - 1)

        return Vec3(0.0, 0.0, 0.0)

    unit_direction = ray.direction.norm()
    t = 0.5 * (unit_direction.y + 1.0)
    return ((1.0 - t) * Color([1.0, 1.0, 1.0])) + (t * Color([0.5, 0.7, 1.0]))


image_height = 100
image_width = 200
samples_per_pixel = 4
max_depth = 10

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

lookfrom = Vec3(2.0, 2.0, 1.0)
camera = Camera(
    lookfrom, Vec3(0.0, 0.0, -1.0), Vec3(0.0, 1.0, 0.0), 70, image_width / image_height,
)

world = HittableList()

world.objects.append(Sphere(Vec3(0, 0, -1), 0.5, Lambertian(Vec3(0.7, 0.3, 0.3))))
world.objects.append(Sphere(Vec3(0, -100.5, -1), 100, Lambertian(Vec3(0.8, 0.8, 0.0))))
world.objects.append(Sphere(Vec3(1.1, 0, -1), 0.5, Metal(Vec3(0.8, 0.8, 0.8), 0.1)))
world.objects.append(Sphere(Vec3(1.1, 0, -1), 0.5, Dialectric(1.5)))


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

    for i in range(image_width - 1):
        pixels[i, image_height - j - 1] = tuple(drawPixel(j, i))

    """
    with Pool() as pool:

        func = partial(drawPixel, j)
        colors = pool.map(func, range(image_width - 1))

        for i in range(image_width - 1):
            pixels[i, image_height - j - 1] = tuple(colors[i])
    """


for j in range(image_height - 1):
    drawRow(j)
    print("{} / {}".format(j + 1, image_height), end="\r")

img.show()
