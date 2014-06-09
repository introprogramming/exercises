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
screenSize = (BLOCK_SIZE * WIDTH, BLOCK_SIZE * HEIGHT)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption(TITLE)

# Initiating the clock
clock = pygame.time.Clock()
ticks = 0
bypassTicks = False

# Initiating matrix for block positions
blocks = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

# Creating the first Tetris object
currentObject = TetrisObject()

################
## Functions

def removeCompleteRows(blocks):
    """Removes all completed rows and
    adds empty rows at the top"""
    
    newBlocks = blocks
    for y in range(len(newBlocks)):
        rowComplete = True
        #If an empty space is found in the row it is not complete
        for x in range(len(newBlocks[y])):
            if not newBlocks[y][x]:
                rowComplete = False
        if rowComplete:
            # If it is complete, add an empty row at top and move down the rows
            newBlocks = [[0 for i in range(WIDTH)]] + newBlocks[0:y] + newBlocks[y+1:]
    return newBlocks

def draw():
    """Clears and draws objects to the screen"""

    screen.fill(WHITE)

    objectPos = currentObject.getPos()
    
    # Draw the Tetris object
    for i in range(len(objectPos)):
        pygame.draw.rect(screen,
                         currentObject.color,
                        [objectPos[i][0] * BLOCK_SIZE,
                         objectPos[i][1] * BLOCK_SIZE,
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
    

def handleInput():
    """Handles the input"""
    
    # Global variables that might be changed
    global bypassTicks
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                currentObject.moveX(-1, blocks)
            elif event.key == pygame.K_RIGHT:
                currentObject.moveX(1, blocks)
            elif event.key == pygame.K_DOWN:
                bypassTicks = True
            elif event.key == pygame.K_UP:
                currentObject.rotate(blocks)
    
def update():
    """Updates the game logic"""

    # Global variables that might be changed
    global bypassTicks
    global ticks
    global currentObject
    global blocks
    global running
    
    # If it is  time to move the current object downward
    if bypassTicks or ticks >= UPDATES_PER_SEC * TICK_TIME:
        # If moving is not successful (collision)
        if not currentObject.moveY(blocks):
            # Stop "fast-forward"
            bypassTicks = False
            
            objectPos = currentObject.getPos()
            
            # For every block occupied by the Tetris object, mark it
            for i in range(len(objectPos)):
                blocks[objectPos[i][1]][objectPos[i][0]] = 1
               
            # Create a new Tetris object
            currentObject = TetrisObject()
            
            objectPos = currentObject.getPos()
            # Check if the new object is obstructed by marked positions, if it is
            # the game is over
            for i in range(len(objectPos)):
                if blocks[objectPos[i][1]][objectPos[i][0]]:
                    running = False
                    
            # Remove completed rows
            blocks = removeCompleteRows(blocks)
        ticks = 0
        
# Start the game
running = True

###############
## Game loop

while running:
    # Handle logic
    handleInput()
    update()
    
    # Draw to the screen
    draw()
    pygame.display.flip()
    
    # Tick...
    ticks += 1
    clock.tick(UPDATES_PER_SEC)