from vec3 import Vec3
from hittable import HittableList
from sphere import Sphere
from camera import Camera
from material import Lambertian, Metal, Dialectric
from render import pixel

from PIL import Image
from functools import partial
import datetime
import multiprocessing


image_height = 1000
image_width = 1500
samples_per_pixel = 50
max_depth = 4

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

camera = Camera(
    Vec3(3.0, 1.0, 2.0),
    Vec3(0.0, 0.0, -1.0),
    Vec3(0.0, 1.0, 0.0),
    70,
    image_width,
    image_height,
)

world = HittableList()

world.objects.append(Sphere(Vec3(0, -100, -1), 100, Lambertian(Vec3(0.4, 0.4, 0.4))))
world.objects.append(Sphere(Vec3(0, 0.8, -1), 0.8, Lambertian(Vec3(0.7, 0.3, 0.2))))
world.objects.append(Sphere(Vec3(0, 1, -3), 1, Metal(Vec3(0.8, 0.8, 0.8), 0.1)))
world.objects.append(Sphere(Vec3(0.5, 0.5, 0.4), 0.5, Dialectric(1.5)))

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
img.save("images/{}.jpg".format(datetime.datetime.today()), "JPEG")
