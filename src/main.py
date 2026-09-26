import pygame
from renderer import *
from OpenGL.GL import *
from pygame.locals import *

pygame.init()

width = 1920
height = 1080

screen = pygame.display.set_mode(
    (width, height),
    DOUBLEBUF | OPENGL
)

aspect_ratio = width / height

glOrtho(
    -aspect_ratio, aspect_ratio,
    -1,1,
    -1,1
)

pygame.display.set_caption("Teleia Physis")

glClearColor(1.0, 0.95, 0.85, 1.0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    pygame.display.flip()

pygame.quit()