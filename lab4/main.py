import numpy as np
import math

import pygame, sys, math
pygame.init()
size = 600
screen = pygame.display.set_mode((size+500,size))
clock = pygame.time.Clock()

BLACK =(0,0,0)
WHITE =(255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


"""
Xp =  (D * X) / Z
Yp =  (D * Y) / Z
"""

DISTANCE = 100

DEFAULT = 100
CUB_SIZE = DEFAULT + 30
Z = 100;

points = [
    # [DEFAULT,DEFAULT,DEFAULT],
    # [CUB_SIZE,DEFAULT,DEFAULT],
    # [DEFAULT,CUB_SIZE,DEFAULT],
    # [DEFAULT,DEFAULT,CUB_SIZE],

    # [CUB_SIZE,CUB_SIZE,DEFAULT],
    # [CUB_SIZE,CUB_SIZE,CUB_SIZE],
    # [DEFAULT,CUB_SIZE,CUB_SIZE],
    # [CUB_SIZE,DEFAULT,CUB_SIZE]

    [DEFAULT,DEFAULT,Z],
    [-DEFAULT,-DEFAULT,Z],
    [-DEFAULT,DEFAULT,Z],
    [DEFAULT,-DEFAULT,Z],

    [DEFAULT,DEFAULT,-Z],
    [-DEFAULT,-DEFAULT,-Z],
    [-DEFAULT,DEFAULT,-Z],
    [DEFAULT,-DEFAULT,-Z]

]

for x in range(int(DEFAULT/1)):
    points.append([x*1,DEFAULT,Z])
    points.append([-x*1,DEFAULT,Z])

    points.append([x*1,-DEFAULT,Z])
    points.append([-x*1,-DEFAULT,Z])
    

    points.append([x*1,DEFAULT,-Z])
    points.append([-x*1,DEFAULT,-Z])

    points.append([x*1,-DEFAULT,-Z])
    points.append([-x*1,-DEFAULT,-Z])

    ########################
    points.append([DEFAULT,DEFAULT,x*1])
    points.append([DEFAULT,DEFAULT,-x*1])

    points.append([DEFAULT,-DEFAULT,x*1])
    points.append([DEFAULT,-DEFAULT,-x*1])

    points.append([-DEFAULT,DEFAULT,x*1])
    points.append([-DEFAULT,DEFAULT,-x*1])

    points.append([-DEFAULT,-DEFAULT,x*1])
    points.append([-DEFAULT,-DEFAULT,-x*1])
    


for x in range(int(DEFAULT/1)):
    points.append([DEFAULT,x*1,Z])
    points.append([DEFAULT,-x*1,Z])

    points.append([-DEFAULT,x*1,Z])
    points.append([-DEFAULT,-x*1,Z])

    points.append([DEFAULT,x*1,-Z])
    points.append([DEFAULT,-x*1,-Z])

    points.append([-DEFAULT,x*1,-Z])
    points.append([-DEFAULT,-x*1,-Z])




def rotate1(angle, point):
    A = [
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle),  math.cos(angle)]
    ]
    B = [
        [point[0]],
        [point[1]]
    ]

    C = np.matmul(A,B)
    return [C[0][0], C[1][0], point[2]]

def rotate2(angle, point):
    A = [
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle),  math.cos(angle)]
    ]
    B = [
        [point[1]],
        [point[2]]
    ]

    C = np.matmul(A,B)
    return [point[0],C[0][0], C[1][0]]

# points[0] = rotate2(0.5,points[0])

a = 0
i = True
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)
    
    #Set and print FPS
    clock.tick(6)
    # print(
        # clock.get_fps()
    # )
    a+=0.1
    # points[0] = rotate2(a,points[0])
    if i: 
        Color = GREEN

        for p in points:
            # p = rotate1(a,p)
            p = rotate2(a,p)

            fake_Z = p[2] + Z + Z


            pos = (
                DISTANCE * p[0] / fake_Z,
                DISTANCE * p[1] / fake_Z,
            )

            # pos = (
            #     p[0],
            #     p[1],
            # )
            # print(pos[0]+ 300,pos[1]);
            pygame.draw.circle(screen, Color, (pos[0]+ 300,pos[1] + 300),1)
        # i = False

        pygame.display.flip()


