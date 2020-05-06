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


# ~ Image Configuration ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Image resolution (dimensions in pixels)
image_height = 1000
image_width = 1500

# Antialiasing (number of rays to cast per pixel)
samples_per_pixel = 50

# Limit on the number of reflections
max_depth = 4

img = Image.new("RGB", (image_width, image_height), "black")
pixels = img.load()

# ~ Camera Configuration ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

camera = Camera(
    # Camera location in 3d space
    Vec3(3.0, 1.0, 2.0),
    # Location for the camera to point at
    Vec3(0.0, 0.0, -1.0),
    # Direction of "up" for the camera
    Vec3(0.0, 1.0, 0.0),
    # Vertical field of view
    70,
    # Image dimensions
    image_width,
    image_height,
)

# ~ Scene Configuration ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

world = HittableList()

world.objects.append(
    # Object to add (only spheres are supported right now)
    Sphere(
        # Location of the sphere in 3d space
        Vec3(0, -100, -1),
        # Radius of the sphere
        100,
        # Material of the sphere (lambertian is just diffuse)
        Lambertian(
            # Color of the material (RGB)
            Vec3(0.4, 0.4, 0.4)
        ),
    )
)
world.objects.append(
    Sphere(
        Vec3(0, 1, -3),
        1,
        # Metal sphere
        Metal(
            # Tint of the metal
            Vec3(0.8, 0.8, 0.8),
            # "Blurriness"
            0.1,
        ),
    )
)
world.objects.append(
    Sphere(
        Vec3(0.5, 0.5, 0.4),
        0.5,
        # Transperent sphere
        Dialectric(
            # Refraction coefficient (1 for air)
            1.5
        ),
    )
)
world.objects.append(Sphere(Vec3(0, 0.8, -1), 0.8, Lambertian(Vec3(0.7, 0.3, 0.2))))
# Add more objects here!

# ~ Rendering ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
