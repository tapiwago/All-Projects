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
    
    
def lineSegment ():

    glClear (GL_COLOR_BUFFER_BIT);
    #Clear previous redering on the display window
    glColor(1.0, 0.0, 0.0);
    
    glBegin (GL_LINES);
    #Specify line-segment geometry. in this case we are are using a line primitive
    glVertex2i (180, 15);       
    glVertex(10, 145);
    glEnd ( );
    glFlush ( ); 


main()
