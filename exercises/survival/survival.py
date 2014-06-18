
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
board = game_object.Board(WIDTH, HEIGHT)
sprites = pygame.sprite.Group()
main_char = game_object.Character(board)

def draw():
    """Clears and draws objects to the screen"""
    global screen
    global sprites
    
    screen.fill(WHITE)

    sprites.draw(screen)
    pygame.display.flip()

def shoot():
    global main_char
    global board
    global sprites
    
    p = game_object.Projectile(board)
    p.set_board_position( (main_char.board_x, main_char.board_y) )
    
    (tx, ty) = pygame.mouse.get_pos()
    p.set_target(tx, ty)
    sprites.add(p)

def handle_input():
    """Handles the input"""
    
    # Global variables that might be changed
    global running
    global main_char
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_char.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                main_char.move(1, 0)
            elif event.key == pygame.K_DOWN:
                main_char.move(0, 1)
            elif event.key == pygame.K_UP:
                main_char.move(0, -1)
            elif event.key == pygame.K_SPACE:
                shoot()
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                main_char.stop(-1, 0)
            elif event.key == pygame.K_RIGHT:
                main_char.stop(1, 0)
            elif event.key == pygame.K_DOWN:
                main_char.stop(0, 1)
            elif event.key == pygame.K_UP:
                main_char.stop(0, -1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shoot()
    
def update():
    """Updates the game logic"""
    global running
    global sprites
    global board
    global main_char
    
    time = 1.0 / UPDATES_PER_SEC
    
    board.set_screen_position(main_char.board_x, main_char.board_y)
    
    for s in sprites:
        s.update(time)

def main():
    
    # Start the game
    global running
    running = True
    
    global sprites
    global main_char
    global board
    
    sprites.add(main_char)
    main_char.set_board_position( board.board_position_of( WIDTH/2, HEIGHT/2) )
    other_char = game_object.Character(board)
    other_char.set_board_position( (550, 500) )
    sprites.add(other_char)
    
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