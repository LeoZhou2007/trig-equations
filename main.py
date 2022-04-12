from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
# import sys
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-20.0, 360.0, -2.0, 2.0)


def drawBackground():
    glBegin(GL_QUADS)
    glVertex2f(-20, -2)
    glVertex2f(360, -2)
    glVertex2f(360, 2)
    glVertex2f(-20, 2)
    glEnd()


def drawGrid():
    glLineWidth(2)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    # X axis
    glVertex2f(-20, 0)
    glVertex2f(360, 0)
    # Y axis
    glVertex2f(0, -2)
    glVertex2f(0, 2)
    glEnd()

    glLineWidth(1)
    glBegin(GL_LINES)
    for x in arange(0, 360, 30):
        glVertex2f(x, -2)
        glVertex2f(x, 2)
    for y in arange(-2, 2, 0.1):
        glVertex2f(-20, y)
        glVertex2f(360, y)
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
    glutCreateWindow('Trig Equations')

    glutDisplayFunc(drawFunc)
    glutIdleFunc(drawFunc)

    init()
    glutMainLoop()
