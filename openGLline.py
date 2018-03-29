import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("A straight line")
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(0.0, 300.0, 0.0, 200.0)
    lineSegment()
    pygame.display.flip()
    pygame.time.wait(0)
