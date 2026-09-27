import pygame
from renderer import *
from physics import *
from OpenGL.GL import *
from pygame.locals import *

pygame.init()

width = 1920
height = 1080

color1 = Color( 1, 0, 0)

radius = 0.1

screen = pygame.display.set_mode(
    (width, height),
    DOUBLEBUF | OPENGL
)

aspect_ratio = width / height

glOrtho(
    -aspect_ratio, aspect_ratio,
    -1, 1,
    -1, 1
)

pygame.display.set_caption("Teleia Physis")
glClearColor(1.0, 0.95, 0.85, 1.0)

gravity = -9.81
position = Vector2(0, 1 - radius)
velocity = Vector2(-1, 0)

ball = PhysicsObject(position, velocity)
ball.acceleration = Vector2(0, gravity)

clock = pygame.time.Clock()
running = True
print(aspect_ratio)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0

    ball.update(dt, aspect_ratio, radius)

    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle(radius, ball.position, 64, color1)
    pygame.display.flip()

pygame.quit()