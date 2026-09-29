from OpenGL.GL import *
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Colour:
    def __init__(self, r, g, b, alpha):
        self.r = r
        self.g = g
        self.b = b
        self.alpha = alpha

def draw_triangle(a, b, c, colour):
    glBegin(GL_TRIANGLES)

    glColor4f(colour.r / 255, colour.g / 255, colour.b/ 255, colour.alpha)

    glVertex2f(a.x, a.y)
    glVertex2f(b.x, b.y)
    glVertex2f(c.x, c.y)

    glEnd()

def draw_quad(a, b, colour):
    glBegin(GL_TRIANGLES)

    glColor4f(colour.r / 255, colour.g / 255, colour.b / 255, colour.alpha)

    glVertex2f(a.x, a.y)
    glVertex2f(b.x, b.y)
    glVertex2f(b.x, a.y)

    glVertex2f(a.x, a.y)
    glVertex2f(b.x, b.y)
    glVertex2f(a.x, b.y)

    glEnd()

def draw_circle(r, c, segments, colour):
    glBegin(GL_TRIANGLE_FAN)

    glColor4f(colour.r / 255, colour.g / 255, colour.b / 255, colour.alpha)

    glVertex2f(c.x, c.y)

    for i in range(segments+1):
        angle = 2 * math.pi * i / segments

        x = c.x + r * math.cos(angle)
        y = c.y + r * math.sin(angle)

        glVertex2f(x,y)
    glEnd()

def draw_line(a, b, colour):
    glBegin(GL_LINES)

    glColor4f(colour.r / 255, colour.g / 255, colour.b / 255, colour.alpha)

    glVertex2f(a.x, a.y)
    glVertex2f(b.x, b.y)

    glEnd()