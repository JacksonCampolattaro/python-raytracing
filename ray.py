from PIL import Image

imageHeight = 250
imageWidth = 250

img = Image.new("RGB", (imageHeight, imageWidth), "black")
pixels = img.load()

for y in range(img.size[0]):
    print("Rendering column ", y)
    for x in range(img.size[1]):
        pixels[y, x] = (y, x, 100)


img.show()
