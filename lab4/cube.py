def start_cube(cube_state):
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


    DEFAULT = 1000
    CUB_SIZE = DEFAULT + 30


    PROJECT_DISTANCE = 600
    REAL_DISTANCE = 6000

    Points = [
        [DEFAULT,DEFAULT,DEFAULT,GREEN],
        [-DEFAULT,DEFAULT,DEFAULT,GREEN],
        [-DEFAULT,-DEFAULT,DEFAULT,GREEN],
        [DEFAULT,-DEFAULT,DEFAULT,GREEN],
        

        [DEFAULT,DEFAULT,-DEFAULT,GREEN],
        [-DEFAULT,DEFAULT,-DEFAULT,GREEN],
        [-DEFAULT,-DEFAULT,-DEFAULT,GREEN],
        [DEFAULT,-DEFAULT,-DEFAULT,GREEN]
    ]

    angles = [0,0,math.pi/6]
    m = 100 




    def rotate_x_y(angle, point):
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

    def rotate_y_z(angle, point):
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

    def rotate_x_z(angle, point):
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



    def rotate_all(points,angles):
        i = 0
        while i < len(points): 
            points[i] = rotate_x_y(angles[0],points[i]) 
            points[i] = rotate_x_z(angles[1],points[i])
            points[i] = rotate_y_z(angles[2],points[i]) 
            i+=1

        return points


    def sort_by_z(all_po):
        x = 0
        # y = 0
        while (x < len(all_po)):
            y = 0
            while (y < len(all_po) - 1):
                    max_1 = -2000000
                    i = 0
                    while i < len(all_po[y]) - 1:
                        if max_1 < all_po[y][i][2]:
                            max_1 = all_po[y][i][2]
                        i+=1
                    
                    max_2 = -2000000
                    i = 0
                    while i < len(all_po[y+1]) - 1:
                        if max_2 < all_po[y+1][i][2]:
                            max_2 = all_po[y+1][i][2]
                        i+=1

                    if max_1 <= max_2:
                        # print("yes")
                        all_po.insert(y+2, all_po[y])
                        all_po.pop(y)

                    y+=1
            x+=1
        return all_po

    def project_points(point):

        fake_Z = point[2] + DEFAULT + 600
        fake_Z += REAL_DISTANCE

        pos = (
            PROJECT_DISTANCE * point[0] / fake_Z + 300,
            PROJECT_DISTANCE * point[1] / fake_Z + 300
        )
        return pos

    def set_groups(Points_Groups,Rotated_Points):
        Points_Groups.append([
            Rotated_Points[0], 
            Rotated_Points[1],
            Rotated_Points[2],
            Rotated_Points[3],
            GREEN
        ])
        Points_Groups.append([
            Rotated_Points[4], 
            Rotated_Points[5],
            Rotated_Points[6],
            Rotated_Points[7],
            BLUE
        ])
        Points_Groups.append([
            Rotated_Points[2], 
            Rotated_Points[6],
            Rotated_Points[7],
            Rotated_Points[3],
            RED
        ])
        Points_Groups.append([
            Rotated_Points[0], 
            Rotated_Points[4],
            Rotated_Points[5],
            Rotated_Points[1],
            B1
        ])
        Points_Groups.append([
            Rotated_Points[0], 
            Rotated_Points[4],
            Rotated_Points[7],
            Rotated_Points[3],
            B2
        ])
        Points_Groups.append([
            Rotated_Points[1], 
            Rotated_Points[5],
            Rotated_Points[6],
            Rotated_Points[2],
            WHITE
        ])
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(BLACK)
        
        #Set and print FPS
        clock.tick(cube_state.FPS)
        # print(
            # clock.get_fps()
        # )


        Rotated_Points = Points.copy()
        rotate_all(Rotated_Points,angles)
        if cube_state.X_Y == True:
            angles[0] += 0.1
            if angles[0] > 2*math.pi:
                angles[0] -= 2*math.pi
            
        if cube_state.X_Z == True:
            angles[1] += 0.1
            if angles[1] > 2*math.pi:
                angles[1] -= 2*math.pi

        if cube_state.Y_Z == True:
            angles[2] += 0.1
            if angles[2] > 2*math.pi:
                angles[2] -= 2*math.pi

        Points_Groups = []
        set_groups(Points_Groups, Rotated_Points)
        sort_by_z(Points_Groups)

        for group in Points_Groups:
            

            if cube_state.Color == "Green":
                color = GREEN
            elif cube_state.Color == "Blue":
                color = BLUE
            elif cube_state.Color == "Red":
                color = RED
            else:
                color = group[-1]
            
            new_group = []
            i = 0 
            while i < len(group) - 1:
                new_group.append(project_points(group[i]))
                i+=1
            # print(new_group)
                
            if cube_state.Color != "None":
                pygame.draw.polygon(
                    screen, 
                    color, 
                    new_group
                )
            else:
                for i in new_group:
                    pygame.draw.circle(
                        screen, 
                        GREEN, 
                        i,
                        10
                    )
                
        pygame.display.flip()
        
