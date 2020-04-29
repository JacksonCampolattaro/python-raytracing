from PIL import Image
from vec3 import Vec3


imageHeight = 250
imageWidth = 250

img = Image.new("RGB", (imageHeight, imageWidth), "black")
pixels = img.load()

for y in range(img.size[0]):
    print("Rendering column ", y, end="\r")
    for x in range(img.size[1]):
        color = Vec3([x / imageWidth, y / imageHeight, 0.2])
        pixels[y, x] = tuple(color)


img.show()
