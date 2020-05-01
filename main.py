from vec3 import Vec3
from hittable import HittableList
from sphere import Sphere
from camera import Camera
from material import Lambertian, Metal, Dialectric
from render import ray_color, sample, pixel

from PIL import Image
from functools import partial
import random
import multiprocessing


image_height = 200
image_width = 300
samples_per_pixel = 40
max_depth = 10

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

camera = Camera(
    Vec3(0.0, 0.0, 1.0),
    Vec3(0.0, 0.0, -1.0),
    Vec3(0.0, 1.0, 0.0),
    70,
    image_width,
    image_height,
)

world = HittableList()

world.objects.append(Sphere(Vec3(0, 0, -1), 0.5, Lambertian(Vec3(0.7, 0.3, 0.3))))
world.objects.append(Sphere(Vec3(0, -100.5, -1), 100, Lambertian(Vec3(0.8, 0.8, 0.0))))
world.objects.append(Sphere(Vec3(1.1, 0, -1), 0.5, Metal(Vec3(0.8, 0.8, 0.8), 0.1)))
world.objects.append(Sphere(Vec3(-1.1, 0, -1), 0.5, Dialectric(1.5)))

pool = multiprocessing.Pool()

for j in range(image_height - 1):

    func = partial(pixel, world, camera, samples_per_pixel, j)

    colors = pool.map(func, range(image_width - 1))
    colors = list(colors)

    for i in range(image_width - 1):
        color = colors[i]
        pixels[i, image_height - j - 1] = tuple(color)

    print("{} / {}".format(j + 1, image_height), end="\r")

img.show()
