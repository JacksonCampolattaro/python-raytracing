from PIL import Image
from vec3 import Vec3
from color import Color
from ray import Ray
from hittable import Hittable
from sphere import Sphere
import math


def hit_sphere(center, radius, ray):

    oc = ray.origin - center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * oc.dot(ray.direction)
    c = oc.dot(oc) - radius * radius
    discriminant = b * b - 4.0 * a * c

    if discriminant < 0:
        return -1.0

    return (-b - math.sqrt(discriminant)) / (2.0 * a)


def ray_color(ray):

    t = hit_sphere(Vec3([0, 0, -1]), 0.5, ray)

    if t > 0.0:
        N = (ray.at(t) - Vec3([0, 0, -1])).norm()
        return Color(0.5 * (N + [1, 1, 1]))

    unit_direction = ray.direction.norm()
    t = 0.5 * (unit_direction.y + 1.0)
    return ((1.0 - t) * Color([1.0, 1.0, 1.0])) + (t * Color([0.5, 0.7, 1.0]))


image_height = 100
image_width = 200

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

lower_left_corner = Vec3([-2.0, -1.0, -1.0])
horizontal = Vec3([4.0, 0.0, 0.0])
vertical = Vec3([0.0, 2.0, 0.0])
origin = Vec3([0.0, 0.0, 0.0])

for j in range(image_height - 1):
    for i in range(image_width - 1):

        u = i / image_width
        v = j / image_height

        r = Ray(origin, lower_left_corner + u * horizontal + v * vertical)

        color = ray_color(r)
        pixels[i, image_height - j - 1] = tuple(color)

    print("{} / {}".format(j + 1, image_height), end="\r")

img.show()
