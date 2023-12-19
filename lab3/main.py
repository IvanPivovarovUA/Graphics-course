from PIL import Image
import numpy as np
import math

DATASET_NAME = 'DS9'
width = 960
height = 540
value1 = (0, 0, 0)

img  = Image.new( mode = "RGB", size = (width, height), color = (255, 255, 255))

with open(DATASET_NAME + '.txt') as f:
    for li in f:
        xy = li.split()
        xy = (int(xy[1]), 540 - int(xy[0]))
        print(xy)
        img.putpixel(xy, value1)
f.close
img.show()
img.save(DATASET_NAME + "-image.jpg")

print("---------------------------------------")
angl =  math.pi / 6
value2 = (0, 0, 255)
img_rot = Image.new( mode = "RGB", size = (width, width), color = (255, 255, 255))
with open(DATASET_NAME + '.txt') as f:
    for li in f:
        xy = li.split()
        xi = float(xy[1]);
        yi = 540 - float(xy[0]);

        A = [
            [xi,yi,1]
        ]
        B = [
            [ math.cos(angl), math.sin(angl), 0],
            [-math.sin(angl), math.cos(angl), 0],
            [     0,              0,          1]
        ]

        
        C = np.matmul(A,B)
        # print(B)
        print(C)
        x = int(C[0][0])
        y = int(C[0][1])
        if (x > 0 and y > 0):
            if (x < 960 and y < 960):
                img_rot.putpixel((x,y), value2)
        # break
f.close
img_rot.show()
img_rot.save(DATASET_NAME + "-afin-rot.jpg")