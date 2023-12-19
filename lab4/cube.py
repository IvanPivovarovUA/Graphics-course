import pygame, sys, math
pygame.init()
size = 600
screen = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()

center = size/2 - 1
black =(0,0,0)
red = (250,0,0)
green = (0,250,0)

diagonal = 100
d = 50



a = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)

    clock.tick(120)
    if a >10000:
        a = 0

    a +=1
    
    angleX = math.radians(a)
    angleY = math.radians(a)
    # print(angle)

    cube_center = {
        'x': center,
        'y': center,
        'z': center,
        'H':50
    }
    Hight = d*cube_center['H']/cube_center['z']
    pygame.draw.circle(
        screen, red, 
        (cube_center['x'],cube_center['y']),
        Hight
    )

    cube_tops = []
    for i in range(4):
        r = diagonal/math.sqrt(3)
        b = diagonal/math.sqrt(3)*math.sqrt(2)
        y = r 
        z = b*math.sin(angleX + i*math.pi/2)
        l = math.sqrt(y**2 +z**2)

        cube_tops.append(
            {
                'x': b*math.cos(angleX + i*math.pi/2),
                'y': l*math.cos(math.atan(z/y) + angleY),
                'z': -l*math.sin(math.atan(z/y) + angleY)
            }

        )
    for i in range(4):
        r = diagonal/math.sqrt(3)
        b = diagonal/math.sqrt(3)*math.sqrt(2)
        y = r 
        z = b*math.sin(angleX + i*math.pi/2)
        l = math.sqrt(y**2 +z**2)

        cube_tops.append(
            {
                'x': -b*math.cos(angleX + i*math.pi/2),
                'y': l*math.cos(math.atan(z/y) + angleY -math.pi),
                'z': -l*math.sin(math.atan(z/y) + angleY -math.pi)
            }

        )




    Hight = d*cube_center['H']/cube_center['z']
    o = 0
    for top in cube_tops:
        o=o+1
        if o<5:
            pygame.draw.circle(
                screen, red, 
                (
                    cube_center['x'] + top['x'],
                    cube_center['y'] + top['y']
                ),
                d*cube_center['H']/(cube_center['z'] + top['z'])
            )
        else:
            pygame.draw.circle(
                screen, red, 
                (
                    cube_center['x'] + top['x'],
                    cube_center['y'] + top['y']
                ),
                d*cube_center['H']/(cube_center['z'] + top['z'])
            )


    pygame.display.flip()


