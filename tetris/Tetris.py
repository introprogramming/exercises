import pygame
from TetrisObject import TetrisObject

# Defining colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Defining game properties
TITLE = "Tetris"
BLOCK_SIZE = 30
WIDTH = 10
HEIGHT = 20
UPDATES_PER_SEC = 60 # Updates per second
TICK_TIME = 0.5 # Seconds per tick

# Initiating the window
pygame.init()
screen_size = (BLOCK_SIZE * WIDTH, BLOCK_SIZE * HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(TITLE)

# Initiating the clock
clock = pygame.time.Clock()
ticks = 0
bypass_ticks = False

# Initiating matrix for block positions
blocks = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

# Creating the first Tetris object
current_object = TetrisObject()

################
## Functions

def remove_complete_rows(blocks):
    """Removes all completed rows and
    adds empty rows at the top"""
    
    new_blocks = blocks
    for y in range(len(new_blocks)):
        row_complete = True
        #If an empty space is found in the row it is not complete
        for x in range(len(new_blocks[y])):
            if not new_blocks[y][x]:
                row_complete = False
        if row_complete:
            # If it is complete, add an empty row at top and move down the rows
            new_blocks = [[0 for i in range(WIDTH)]] + new_blocks[0:y] + new_blocks[y+1:]
    return new_blocks

def draw():
    """Clears and draws objects to the screen"""

    screen.fill(WHITE)

    object_pos = current_object.get_pos()
    
    # Draw the Tetris object
    for i in range(len(object_pos)):
        pygame.draw.rect(screen,
                         current_object.color,
                        [object_pos[i][0] * BLOCK_SIZE,
                         object_pos[i][1] * BLOCK_SIZE,
                         BLOCK_SIZE,
                         BLOCK_SIZE], 0)
    
    # Draw the blocks
    for y in range(len(blocks)):
        for x in range(len(blocks[0])):
            if blocks[y][x] == 1:
                pygame.draw.rect(screen,
                                 RED,
                                [x * BLOCK_SIZE,
                                 y * BLOCK_SIZE,
                                 BLOCK_SIZE,
                                 BLOCK_SIZE], 0)
    

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
                current_object.move_x(-1, blocks)
            elif event.key == pygame.K_RIGHT:
                current_object.move_x(1, blocks)
            elif event.key == pygame.K_DOWN:
                bypass_ticks = True
            elif event.key == pygame.K_UP:
                current_object.rotate(blocks)
    
def update():
    """Updates the game logic"""

    # Global variables that might be changed
    global bypass_ticks
    global ticks
    global current_object
    global blocks
    global running
    
    # If it is  time to move the current object downward
    if bypass_ticks or ticks >= UPDATES_PER_SEC * TICK_TIME:
        # If moving is not successful (collision)
        if not current_object.move_y(blocks):
            # Stop "fast-forward"
            bypass_ticks = False
            
            object_pos = current_object.get_pos()
            
            # For every block occupied by the Tetris object, mark it
            for i in range(len(object_pos)):
                blocks[object_pos[i][1]][object_pos[i][0]] = 1
               
            # Create a new Tetris object
            current_object = TetrisObject()
            
            object_pos = current_object.get_pos()
            # Check if the new object is obstructed by marked positions, if it is
            # the game is over
            for i in range(len(object_pos)):
                if blocks[object_pos[i][1]][object_pos[i][0]]:
                    running = False
                    
            # Remove completed rows
            blocks = remove_complete_rows(blocks)
        ticks = 0
        
# Start the game
running = True

###############
## Game loop

while running:
    # Handle logic
    handle_input()
    update()
    
    # Draw to the screen
    draw()
    pygame.display.flip()
    
    # Tick...
    ticks += 1
    clock.tick(UPDATES_PER_SEC)