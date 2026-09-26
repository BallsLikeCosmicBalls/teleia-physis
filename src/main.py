import pygame
import pygame_gui
from OpenGL.GL import *
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(
    (800, 600),
    DOUBLEBUF | OPENGL
)

pygame.display.set_caption("Teleia Physis")

glClearColor(1.0, 0.0, 1.0, 1.0)

manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()
for event in pygame.event.get():
    manager.process_events(event)

time_delta = clock.tick(60) / 1000.0

input_box = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(300, 250, 200, 40),
    manager=manager
)

manager.process_events(event)
manager.update(time_delta)
manager.draw_ui(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)

    glColor3f(0.0, 1.0, 1.0)

    glVertex2f(0, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)

    glEnd()

    pygame.display.flip()

pygame.quit()