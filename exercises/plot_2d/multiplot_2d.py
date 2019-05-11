import math, pygame, plot_2d
from pygame.locals import *

# Extension of plot_2d with functionality to plot multiple functions.

#############################################
## Standard colors (RGB)
BLACK = (20, 20, 40)
WHITE = (255, 255, 255)
BLUE = (20, 20, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (50, 255, 255)


#############################################
## Customize plot here

def functions_to_print():
    """Write list of functions to plot here of the format [f_info1, f_info2, ...], where f_info == (f, color).
    Each function `f` must take a single number x and return a single number y."""
    return [
        (lambda x: -x * (x - 3), GREEN),
        (lambda x: 2 * math.cos(x) - 0.5 * x, CYAN)]


# Imports window settings from plot_2d.py

#############################################
## Let the program calculate the rest

def plot_fun(f_info, X_MIN, X_MAX, N_POINTS, screen):
    """Plots a function `f` with the specified settings.
    
    f_info == (f, color)"""
    cc = plot_2d.curve_coordinates(f_info[0], X_MIN, X_MAX, N_POINTS)
    pp = map(plot_2d.coordinate_to_position, cc)
    plot_2d.draw(screen, pp, f_info[1])


def main():
    """Graphics: draws graphs on window and await EXIT or ESCAPE."""
    pygame.init()
    screen = pygame.display.set_mode([plot_2d.WIDTH, plot_2d.HEIGHT])
    pygame.display.set_caption('Multiplot 2d')

    clock = pygame.time.Clock()

    screen.fill(plot_2d.background_color)

    map(lambda f: plot_fun(f, plot_2d.X_MIN, plot_2d.X_MAX, plot_2d.N_POINTS, screen), functions_to_print())
    plot_2d.draw_axis(screen)

    pygame.display.update()
    while 1:
        e = pygame.event.wait()
        if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
            break

    pygame.quit()


# if Python says run...
if __name__ == '__main__':
    main()
