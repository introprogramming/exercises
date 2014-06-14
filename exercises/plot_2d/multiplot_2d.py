
import math, pygame, plot_2d
from pygame.locals import *

#############################################
## Standard colors (RGB)
BLACK = ( 20,  20,  40)
WHITE = (255, 255, 255)
BLUE =  ( 20,  20, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
CYAN  = ( 50, 255, 255)

#############################################
## Customize plot here

def functions_to_print():
    """Write function to plot here.
    Must take a single number x and return a single number y."""
    return [\
        (lambda(x): -x*(x-3),      GREEN),\
        (lambda(x): 2*math.cos(x)-0.5*x,  CYAN) \
        ]

#Range of window
X_MIN = 0.0
X_MAX = 10.0
Y_MIN = -10.0
Y_MAX = 10.0

#Tick interval on axes
X_TICK = 2.5
Y_TICK = 2.5

#Granularity of plotted functions, more points -> higher resolution plot
N_POINTS = 100

#Colors
background_color = BLACK
grid_color = WHITE

# Note, it is also possible to make a list of functions to print
# and respective colors:
# functions = [(f1, color1), (f2, color2), ...]

#############################################
## Let the program calculate the rest
WIDTH = 640
HEIGHT = 480

X_SIZE = X_MAX-X_MIN
Y_SIZE = Y_MAX-Y_MIN

def plot_fun( f_info, X_MIN, X_MAX, N_POINTS, screen):
    cc = plot_2d.curve_coordinates(f_info[0], X_MIN, X_MAX, N_POINTS)
    pp = map(plot_2d.coordinate_to_position, cc)
    plot_2d.draw(screen, pp, f_info[1])

def main():
    """Graphics: draws graphs on window and await EXIT or ESCAPE."""
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('mini birds')
    
    clock = pygame.time.Clock()

    screen.fill(background_color)
    
    #f = functions_to_print()[0]
    #cc = plot_2d.curve_coordinates(f, X_MIN, X_MAX, N_POINTS)
    #pp = map(plot_2d.coordinate_to_position, cc)
    
    #This would typically be done inside the loop, but since it is never
    #updated: might as well keep it outside
    #plot_2d.draw(screen, pp)
    map(lambda(f): plot_fun(f, X_MIN, X_MAX, N_POINTS, screen), functions_to_print())

    done = False
    while not done:
        time = clock.tick(60)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break

    pygame.quit()

# if Python says run...
if __name__ == '__main__':
    main()
