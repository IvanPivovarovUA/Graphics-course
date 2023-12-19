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

DISTANCE = 1

DEFAULT = 100
CUB_SIZE = DEFAULT + 30

Z = 2;

points = [
    [DEFAULT,DEFAULT,DEFAULT],
    [CUB_SIZE,DEFAULT,DEFAULT],
    [DEFAULT,CUB_SIZE,DEFAULT],
    [DEFAULT,DEFAULT,CUB_SIZE],

    [CUB_SIZE,CUB_SIZE,DEFAULT],
    [CUB_SIZE,CUB_SIZE,CUB_SIZE],
    [DEFAULT,CUB_SIZE,CUB_SIZE],
    [CUB_SIZE,DEFAULT,CUB_SIZE]

    # [DEFAULT,DEFAULT,Z],
    # [-DEFAULT,-DEFAULT,Z],
    # [-DEFAULT,DEFAULT,Z],
    # [DEFAULT,-DEFAULT,Z],

    # [DEFAULT,DEFAULT,Z+2],
    # [-DEFAULT,-DEFAULT,Z+2],
    # [-DEFAULT,DEFAULT,Z+2],
    # [DEFAULT,-DEFAULT,Z+2]

]



def rotate(angle, point):
    A = [
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle),  math.cos(angle)]
    ]
    B = [
        [point[0]],
        [point[1]]
    ]

    C = np.matmul(A,B)
    return (C[0][0], C[1][0], point[2])

    # B = [
    #     [point[1]],
    #     [point[2]]
    # ]

    # C = np.matmul(A,B)
    # return (point[0],C[0][0], C[1][0])


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
    a+=0.1;

    if i: 
        Color = GREEN
        for p in points:
            p = rotate(a,p)

            # pos = (
            #     DISTANCE * p[0] / p[2],
            #     DISTANCE * p[1] / p[2],
            # )

            pos = (
                p[0],
                p[1],
            )
            print(pos[0]+ 300,pos[1]);
            pygame.draw.circle(screen, Color, (pos[0]+200,pos[1]+200),2)
        # i = False
        pygame.display.flip()


