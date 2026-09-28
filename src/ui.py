from OpenGL.GL import *

def draw_button(x, y, width, height, color):
    glColor3f(color.r / 255, color.g / 255, color.b / 255)

    glBegin(GL_QUADS)

    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y - height)
    glVertex2f(x, y - height)

    glEnd()