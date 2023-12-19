from PIL import Image

DATASET_NAME = 'DS5'
width = 960
height = 540

img  = Image.new( mode = "RGB", size = (width, height), color = (255, 255, 255))


value = (0, 0, 0)

with open(DATASET_NAME + '.txt') as f:
    for li in f:
        xy = li.split()
        xy = (int(xy[1]), 540 - int(xy[0]))
        print(xy)
        img.putpixel(xy, value)
f.close

img.show()
img.save(DATASET_NAME + "-image.jpg")