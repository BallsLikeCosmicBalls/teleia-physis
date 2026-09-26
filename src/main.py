import pygame
from renderer import *
from OpenGL.GL import *
from pygame.locals import *

point1 = Point(0.0, 0.5)
point2 = Point(-0.5, -0.5)
point3 = Point(0.5, -0.5)

color = Color(255, 0, 0)

pygame.init()

screen = pygame.display.set_mode(
    (800, 600),
    DOUBLEBUF | OPENGL
)

pygame.display.set_caption("Teleia Physis")

glClearColor(1.0, 0.0, 1.0, 1.0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    draw_triangle(point1, point2, point3,color)

    pygame.display.flip()

pygame.quit()