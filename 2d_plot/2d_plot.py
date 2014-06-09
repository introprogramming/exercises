
import math, pygame
from pygame.locals import *

#############################################
## Standard colors
BLACK = ( 20,  20,  40)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#############################################
## Customize plot
background_color = BLACK
plot_color = GREEN
grid_color = WHITE

X_MIN = 0.0
X_MAX = 10.0
Y_MIN = -10.0
Y_MAX = 10.0

X_TICK = 2.0
Y_TICK = 2.0

N_POINTS = 100

def function_to_print(x):
    return -x*(x-3)
    
# Note, it is also possible to make a list of functions to print
# and respective colors

#############################################
## Let the program calculate the rest
WIDTH = 640
HEIGHT = 480

X_SIZE = X_MAX-X_MIN
Y_SIZE = Y_MAX-Y_MIN

def coordinate_to_position(c):
    """Converts a model coordinate (vector) into a graphic position (pixel)"""
    gx = (c[0]-X_MIN)*WIDTH/X_SIZE
    gy = HEIGHT - (c[1]-Y_MIN)*HEIGHT/Y_SIZE
    return [gx, gy]
    
def curve_coordinates(f, x0, x1, points):
    """Returns list of coordinates
    
    Creates linear splines for this function f, from x0 to x1
    Length of returned list == points."""
    coordinates = []
    x = x0
    delta = (x1-x0)/(points-1)
    while x <= x1:
        coordinates += [[x, f(x)]]
        x += delta
    return coordinates

def linspace(x0, x1, points):
    """Returns a list of numbers of `points` elements, 
    with constant intervals between `x0` and `x1`"""
    delta = (x1-x0)/(points-1)
    return map(lambda(x): x0 + delta*x, range(points))
    
def curve_coordinates2(f, x0, x1, points):
    """Alternative implementation of curve_coordinates(...) above
    
    This is more compact and functional-like but probably slower."""
    
    return [ [x, f(x)] for x in linspace(x0,x1,points)]

def draw_ticks(screen, axis):
    """Draws appropriate ticks on the specified axis.
    axis == 0 -> X-axis, otherwise Y-axis.
    
    This implementation is not so readable, see alternative implementation
    for a more readable one."""
    if axis == 0:
        min = X_MIN
        max = X_MAX
        tick = X_TICK
        limit = HEIGHT
    else:
        axis = 1
        min = Y_MIN
        max = Y_MAX
        tick = Y_TICK
        limit = WIDTH
    
    start = min + min % tick
    end = max - max % tick
    points = (end-start)/tick + 1
    t = limit/120
    
    for x in linspace(start, end, int(points)):
        c=[0,0]
        c[axis] = x
        v = coordinate_to_position(c)
        
        a = v[1-axis]+t
        if(a > limit):
            a = limit
            
        b = v[1-axis]-t
        if(b < 0):
            b = 0
            
        #Copying v
        s=list(v)
        s[1-axis] = a
        
        e=list(v)
        e[1-axis] = b
        pygame.draw.line(screen, grid_color, s, e, 2)
    
def draw_x_ticks(screen):
    """Draws appropriate ticks on the X-axis."""
    start = X_MIN + X_MIN % X_TICK
    end = X_MAX - X_MAX % X_TICK
    points = (end-start)/X_TICK + 1
    
    #t == half length of the tick line
    t = HEIGHT/120
    
    #one iteration per tick
    for x in linspace(start, end, int(points)):
        v = coordinate_to_position([x, 0])
        a = v[1]+t
        b = v[1]-t
        
        if(a > HEIGHT):
            a = HEIGHT
        if(b < 0):
            b = 0
        pygame.draw.line(screen, grid_color,\
            [v[0], a],\
            [v[0], b],\
            2)

def draw_y_ticks(screen):
    """Draws appropriate ticks on the Y-axis.
    This function mirrors draw_x_ticks(...)"""
    start = Y_MIN + Y_MIN % Y_TICK
    end = Y_MAX - Y_MAX % Y_TICK
    points = (end-start)/Y_TICK + 1
    
    t = WIDTH/120
    
    for y in linspace(start, end, int(points)):
        v = coordinate_to_position([0, y])
        #print v
        
        a = v[0]+t
        b = v[0]-t
        
        if(a > WIDTH):
            a = WIDTH
        if(b < 0):
            b = 0
        
        pygame.draw.line(screen, grid_color,\
            [a, v[1]],\
            [b, v[1]],\
            2)

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('mini birds')

    screen.fill(background_color)
    
    cc = curve_coordinates(function_to_print, X_MIN, X_MAX, N_POINTS)
    pp = map(coordinate_to_position, cc)

    done = False
    while not done:
        #Function
        pygame.draw.lines(screen, plot_color, False, pp, 3)
        
        ## Alternative implementations:
        #draw_x_ticks(screen)
        #draw_y_ticks(screen)
        
        draw_ticks(screen, 0)
        draw_ticks(screen, 1)
        
        #X-Axis
        pygame.draw.lines(screen, grid_color, False, map(coordinate_to_position,\
            [[X_MIN, 0],[X_MAX, 0]]), 2)
            
        #Y-Axis
        pygame.draw.lines(screen, grid_color, False, map(coordinate_to_position,\
            [[0, Y_MIN],[0, Y_MAX]]), 2)

        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break

    pygame.quit()

# if Python says run...
if __name__ == '__main__':
    main()
