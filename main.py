from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import math
import decimal

x1 = -20
x2 = 360
y1 = -2
y2 = 2

h_gap = 30
v_gap = decimal.Decimal('0.1')

title = "Trig Equations"

h_start = x1 - x1 % h_gap
h_end = x2 - x2 % h_gap
v_start = y1 - y1 % v_gap
v_end = y2 - y2 % v_gap


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(x1, x2, y1, y2)


def drawBackground():
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()


def drawGrid():
    glLineWidth(1)
    glBegin(GL_LINES)
    for x in arange(h_start, h_end, h_gap):
        glVertex2f(x, y1)
        glVertex2f(x, y2)
    for y in arange(v_start, v_end, v_gap):
        glVertex2f(x1, y)
        glVertex2f(x2, y)
    glEnd()
    glLineWidth(2)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    # X axis
    glVertex2f(x1, 0)
    glVertex2f(x2, 0)
    # Y axis
    glVertex2f(0, y1)
    glVertex2f(0, y2)
    glEnd()


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2.0)
    glLineWidth(2.0)

    glColor3f(1.0, 1.0, 1.0)
    drawBackground()

    glLineWidth(1)
    glColor3f(0.7, 0.7, 0.7)
    drawGrid()

    glBegin(GL_POINTS)
    # cos
    glColor3f(0.0, 0.0, 1.0)
    for x in arange(0.0, 360.0, 0.01):
        y = math.cos(math.radians(x))
        glVertex2f(x, y)

    # sin
    glColor3f(1.0, 0.0, 0.0)
    for x in arange(0.0, 360.0, 0.01):
        y = math.sin(math.radians(x))
        glVertex2f(x, y)

    # tan
    glColor3f(0.0, 1.0, 0.0)
    for x in arange(0.0, 360.0, 0.01):
        y = math.tan(math.radians(x))
        glVertex2f(x, y)
    glEnd()

    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutInitWindowSize(600, 400)
    glutCreateWindow(title)

    glutDisplayFunc(drawFunc)
    glutIdleFunc(drawFunc)

    init()
    glutMainLoop()
