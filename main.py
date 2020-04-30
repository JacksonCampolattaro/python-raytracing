from PIL import Image
from color import Color
from ray import Ray


def ray_color(ray):
    unit_direction = ray.norm()
    t = 0.5 * (unit_direction.y + 1)
    return (1.0 - t) * Color([1, 1, 1]) + t * Color([0.5, 0.7, 1.0])


image_height = 1000
image_width = 2000

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

for j in range(image_height - 1):
    print("{} / {}".format(j + 1, image_height), end="\r")
    for i in range(image_width - 1):
        c = Color([i / image_width, j / image_height, 0.2])
        pixels[i, image_height - j - 1] = tuple(c)

img.show()
