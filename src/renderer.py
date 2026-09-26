from OpenGL.GL import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def draw_triangle(a, b, c, color):
    glBegin(GL_TRIANGLES)

    glColor3f(color.r, color.g, color.b)

    glVertex2f(a.x, a.y)
    glVertex2f(b.x, b.y)
    glVertex2f(c.x, c.y)

    glEnd()