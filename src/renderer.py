from OpenGL.GL import *
import math

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

def draw_quad(a, b, color):
    glBegin(GL_TRIANGLES)

    glColor3f(color.r, color.g, color.b)

    glVertex2f(a.x, a.y)
    glVertex2f(b.x, b.y)
    glVertex2f(b.x, a.y)

    glVertex2f(a.x, a.y)
    glVertex2f(b.x, b.y)
    glVertex2f(a.x, b.y)

    glEnd()

def draw_circle(r, c, segments, color):
    glBegin(GL_TRIANGLE_FAN)

    glColor3f(color.r, color.g, color.b)

    glVertex2f(c.x, c.y)

    for i in range(segments+1):
        angle = 2 * math.pi * i / segments

        x = c.x + r * math.cos(angle)
        y = c.y + r * math.sin(angle)

        glVertex2f(x,y)
    glEnd()