import numpy as np
import math

import pygame, sys, math
pygame.init()
size = 600
screen = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()

BLACK =(0,0,0)
WHITE =(255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

B1 = (110,150,250)
B2 = (255,110,11)
"""
Xp =  (D * X) / Z
Yp =  (D * Y) / Z
"""
REAL_DISTANCE = 6000


DEFAULT = 1000
CUB_SIZE = DEFAULT + 30
Z = 1000

DISTANCE = 600
old_points = [
    # [DEFAULT,DEFAULT,DEFAULT],
    # [CUB_SIZE,DEFAULT,DEFAULT],
    # [DEFAULT,CUB_SIZE,DEFAULT],
    # [DEFAULT,DEFAULT,CUB_SIZE],

    # [CUB_SIZE,CUB_SIZE,DEFAULT],
    # [CUB_SIZE,CUB_SIZE,CUB_SIZE],
    # [DEFAULT,CUB_SIZE,CUB_SIZE],
    # [CUB_SIZE,DEFAULT,CUB_SIZE]

    [DEFAULT,DEFAULT,Z,GREEN],
    [-DEFAULT,DEFAULT,Z,GREEN],
    [-DEFAULT,-DEFAULT,Z,GREEN],
    [DEFAULT,-DEFAULT,Z,GREEN],
    

    [DEFAULT,DEFAULT,-Z,GREEN],
    [-DEFAULT,DEFAULT,-Z,GREEN],
    [-DEFAULT,-DEFAULT,-Z,GREEN],
    [DEFAULT,-DEFAULT,-Z,GREEN]

]

m = 100 

# for x in range(int(DEFAULT/m)):
#     for y in range(int(DEFAULT/m)):
#         points.append([x*m,y*m,Z,GREEN])
#         points.append([-x*m,y*m,Z,GREEN])

#         points.append([x*m,-y*m,Z,GREEN])
#         points.append([-x*m,-y*m,Z,GREEN])

# ###############################################

#         points.append([x*m,y*m,-Z,GREEN])
#         points.append([-x*m,y*m,-Z,GREEN])

#         points.append([x*m,-y*m,-Z,GREEN])
#         points.append([-x*m,-y*m,-Z,GREEN])

# ###############################################

#         points.append([-Z, x*m,y*m,RED])
#         points.append([-Z, -x*m,y*m,RED])

#         points.append([-Z, x*m,-y*m,RED])
#         points.append([-Z,-x*m,-y*m,RED])

# #############################################
#         points.append([Z, x*m,y*m,RED])
#         points.append([Z, -x*m,y*m,RED])

#         points.append([Z, x*m,-y*m,RED])
#         points.append([Z,-x*m,-y*m,RED])

# #############################################
#         points.append([x*m,Z,y*m,BLUE])
#         points.append([-x*m,Z,y*m,BLUE])

#         points.append([x*m,Z,-y*m,BLUE])
#         points.append([-x*m,Z,-y*m,BLUE])
# #############################################
#         points.append([x*m,-Z,-y*m,BLUE])
#         points.append([-x*m,-Z,-y*m,BLUE])

#         points.append([x*m,-Z,y*m,BLUE])
#         points.append([-x*m,-Z,y*m,BLUE])



# for x in range(int(DEFAULT/10)):
#     points.append([x*10,DEFAULT,Z])
#     points.append([-x*10,DEFAULT,Z])

#     points.append([x*10,-DEFAULT,Z])
#     points.append([-x*10,-DEFAULT,Z])
    

#     points.append([x*10,DEFAULT,-Z])
#     points.append([-x*10,DEFAULT,-Z])

#     points.append([x*10,-DEFAULT,-Z])
#     points.append([-x*10,-DEFAULT,-Z])

#     ########################
#     points.append([DEFAULT,DEFAULT,x*10])
#     points.append([DEFAULT,DEFAULT,-x*10])

#     points.append([DEFAULT,-DEFAULT,x*10])
#     points.append([DEFAULT,-DEFAULT,-x*10])

#     points.append([-DEFAULT,DEFAULT,x*10])
#     points.append([-DEFAULT,DEFAULT,-x*10])

#     points.append([-DEFAULT,-DEFAULT,x*10])
#     points.append([-DEFAULT,-DEFAULT,-x*10])
    


# for x in range(int(DEFAULT/10)):
#     points.append([DEFAULT,x*10,Z])
#     points.append([DEFAULT,-x*10,Z])

#     points.append([-DEFAULT,x*10,Z])
#     points.append([-DEFAULT,-x*10,Z])

#     points.append([DEFAULT,x*10,-Z])
#     points.append([DEFAULT,-x*10,-Z])

#     points.append([-DEFAULT,x*10,-Z])
#     points.append([-DEFAULT,-x*10,-Z])




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

def rotate3(angle, point):
    A = [
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle),  math.cos(angle)]
    ]
    B = [
        [point[0]],
        [point[2]]
    ]

    C = np.matmul(A,B)
    return [C[0][0], point[1], C[1][0]]

a = 0
i = True

def rotate_all(points):
    i = 0
    while i < len(points): 
        points[i] = rotate2(0.1,points[i])
        # points[i] = rotate3(a,points[i]) 
        i+=1

    return points

def make_point(p):
    # p = rotate2(a,p)
    # p = rotate2(math.pi/6,p)
    # p = rotate3(a,p)

    fake_Z = p[2] + Z + 600
    fake_Z += REAL_DISTANCE

    pos = (
        DISTANCE * p[0] / fake_Z + 300,
        DISTANCE * p[1] / fake_Z + 300
    )
    return pos 

def check_max(all_po):
    x = 0
    y = 0
    while (x < len(all_po)):
        while (y < len(all_po) - 1):
                max_1 = -200000000
                for i in all_po[y]:
                    if max_1 < i[2]:
                        max_1 = i[2]
                max_2 = -200000000
                for i in all_po[y + 1]:
                    if max_2 < i[2]:
                        max_2 = i[2]

                if max_1 < max_2:
                    all_po.insert(y+2, all_po[y])
                    all_po.pop(y)

                y+=1
        x+=1
    return all_po
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)
    
    #Set and print FPS
    clock.tick(3)
    print(
        # clock.get_fps()
    )
    a+=0.1

    if i: 
        Color = GREEN

        # for p in points:
        #     Color = p[3]

        #     p = rotate3(a,p)
        #     p = rotate2(math.pi/4,p)
        #     # p = rotate2(a,p)

        #     fake_Z = p[2] + Z + 600
        #     fake_Z += REAL_DISTANCE

        #     pos = (
        #         DISTANCE * p[0] / fake_Z,
        #         DISTANCE * p[1] / fake_Z,
        #     )

        #     # pos = (
        #     #     p[0],
        #     #     p[1]
        #     # )
        #     pygame.draw.circle(screen, Color, (pos[0]+ 300,pos[1] + 300),1)
        # i = False
        
        points = rotate_all(old_points)



        all_po = []
        all_po.append([
            points[0], 
            points[1],
            points[2],
            points[3]
        ])
        # pygame.draw.polygon(screen, B1,Po)

        all_po.append([
            points[4], 
            points[5],
            points[6],
            points[7]
        ])
        # pygame.draw.polygon(screen, B1,Po)


        all_po.append([
            points[2], 
            points[6],
            points[7],
            points[3]
        ])
        # pygame.draw.polygon(screen, B1,Po)

        all_po.append([
            points[0], 
            points[4],
            points[5],
            points[1]
        ])
        # pygame.draw.polygon(screen, B1,Po)


        all_po.append([
            points[0], 
            points[4],
            points[7],
            points[3]
        ])
        # pygame.draw.polygon(screen, B1,Po)

        all_po.append([
            points[1], 
            points[5],
            points[6],
            points[2]
        ])
        # pygame.draw.polygon(screen, B1,Po)

        all_po = check_max(all_po)
        
        color_list = [RED,GREEN,WHITE,BLUE,B1,B2,GREEN,GREEN]
        color_list_INDEX =0

        for i in all_po:
            new_i = []
            for y in i:
                new_i.append(make_point(y))
            
            pygame.draw.polygon(screen, color_list[color_list_INDEX], new_i)
            color_list_INDEX +=1

        pygame.display.flip()
    

