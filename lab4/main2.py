import pygame
from pygame.locals import *
from math import *
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Инициализация экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Cube")

clock = pygame.time.Clock()

# Определение вершин куба
vertices = [
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, 1],
    [1, -1, 1]
]

# Определение граней куба
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Определение центра экрана
cx, cy = width // 2, height // 2

# Определение угла поворота куба
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BLACK)

    # Поворот куба
    angle += 0.01
    rotation_matrix_y = [
        [cos(angle), 0, -sin(angle)],
        [0, 1, 0],
        [sin(angle), 0, cos(angle)]
    ]

    rotated_vertices = []
    for vertex in vertices:
        result = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                result[i] += vertex[j] * rotation_matrix_y[j][i]
        rotated_vertices.append(result)

    # Преобразование 3D координат в 2D
    projected_vertices = []
    for vertex in rotated_vertices:
        x = vertex[0] * 200 / (vertex[2] + 5) + cx
        y = vertex[1] * 200 / (vertex[2] + 5) + cy
        projected_vertices.append((x, y))

    # Рисование граней куба
    for edge in edges:
        pygame.draw.line(screen, WHITE, projected_vertices[edge[0]], projected_vertices[edge[1]])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
