import pygame
from renderer import *
from physics import *
from ui import *
from OpenGL.GL import *
from pygame.locals import *

pygame.init()

width = 1920
height = 1080

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

#// variables for test physics object//#

bounce_loss = 0.95
friction = 0.95
gravity = -9.81
position = Vector2(0, 1 - radius)
velocity = Vector2(50, 0)

ball = PhysicsObject(position, velocity)
ball.acceleration = Vector2(0, gravity)

#// pwetty colors!!!! //#

default_object_color = Colour(140, 140, 220, 1)
button_color = Colour(255, 220, 170, 1)
line_color = Colour(20, 20, 20, 1)
menu_color = Colour(0, 0, 255, 0)

#// menu button variables //#

menu_button_x = aspect_ratio - 0.55
menu_button_y = 0.9

menu_button_width = 0.45
menu_button_height = 0.15

#// simulate button variables //#

simulate_button_x = -aspect_ratio + 0.1
simulate_button_y = 0.9

simulate_button_width = 0.45
simulate_button_height = 0.15

#// stuff //#

clock = pygame.time.Clock()

running = True
open_menu = False
simulate = False

while running:

    dt = clock.tick(60) / 1000.0
    dt = min(dt, 0.05) # limit for delta time

    mouse_x, mouse_y = pygame.mouse.get_pos()

    world_x = (mouse_x / width) *(2 * aspect_ratio) - aspect_ratio # convert x-axis mouse coordinates in pixels into coordinates from -1 to 1
    world_y = 1 - (mouse_y / height) *2 # same here just for the y-axis

    if simulate:
        ball.update(dt, aspect_ratio, radius, bounce_loss, friction)

    glClear(GL_COLOR_BUFFER_BIT)

    ball.draw(radius, position, 64, default_object_color)
    draw_button(menu_button_x, menu_button_y, menu_button_width, menu_button_height, button_color)
    draw_button(simulate_button_x, simulate_button_y, simulate_button_width, simulate_button_height, button_color)

    draw_line(ball.position, (ball.velocity * 0.1) + ball.position, line_color)

    if open_menu:
        draw_quad(Point(0.6, -1), Point(1 + aspect_ratio, 1), menu_color)
        print(menu_color.alpha)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_button_x <= world_x <= menu_button_x + menu_button_width:
                if menu_button_y - menu_button_height <= world_y <= menu_button_y: # checks if user is clicking the button or not
                    open_menu = not open_menu

        if event.type == pygame.MOUSEBUTTONDOWN:
            if simulate_button_x <= world_x <= simulate_button_x + simulate_button_width:
                if simulate_button_y - simulate_button_height <= world_y <= simulate_button_y: # checks if user is clicking the button or not
                    simulate = not simulate

    pygame.display.flip()

pygame.quit()