
import pygame
import game_object

# Defining colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Defining game properties
TITLE = "Survival"
WIDTH = 640
HEIGHT = 480
UPDATES_PER_SEC = 60 # Updates per second
TICK_TIME = 0.5 # Seconds per tick

# Initiating the window
pygame.init()
screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(TITLE)

# Initiating the clock
clock = pygame.time.Clock()
ticks = 0
bypass_ticks = False

# Game data
sprites = pygame.sprite.Group()
main_char = game_object.Character()

def draw():
    """Clears and draws objects to the screen"""
    global screen
    global sprites
    
    screen.fill(WHITE)

    sprites.draw(screen)
    pygame.display.flip()

def shoot():
    global main_char
    global sprites
    
    p = game_object.Projectile()
    p.set_position(main_char.rect.x, main_char.rect.y)
    p.set_target(0,0)
    sprites.add(p)

def handle_input():
    """Handles the input"""
    
    # Global variables that might be changed
    global bypass_ticks
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_SPACE:
                shoot()
    
def update():
    """Updates the game logic"""
    global running
    global sprites
    
    time = 1.0 / UPDATES_PER_SEC
    
    for s in sprites:
        s.update(time)

def main():
    
    # Start the game
    global running
    running = True
    
    global sprites
    global main_char
    sprites.add(main_char)
    main_char.set_position(WIDTH/2, HEIGHT/2)
    
    ###############
    ## Game loop
    while running:
        # Handle logic
        handle_input()
        update()
        
        # Draw to the screen
        draw()
        
        # Tick...
        global ticks
        ticks += 1
        clock.tick(UPDATES_PER_SEC)
    
    pygame.quit()


main()