
import pygame, random
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

###############################
# Game data
board = game_object.Board(WIDTH, HEIGHT)
main_char = game_object.Character(board)

sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()
player_projectiles = pygame.sprite.Group()
#monster_projectiles = pygame.sprite.Group()

def draw():
    """Clears and draws objects to the screen"""
    global screen
    global sprites
    
    screen.fill(WHITE)

    sprites.draw(screen)
    pygame.display.flip()

def shoot():
    """Player shoots a projectile."""
    global main_char
    global board
    global sprites
    
    p = game_object.Projectile(board)
    p.set_board_position( (main_char.board_x, main_char.board_y) )
    
    (tx, ty) = pygame.mouse.get_pos()
    p.set_target(tx, ty)
    sprites.add(p)
    player_projectiles.add(p)

def handle_input():
    """Handles the input
    
    Arrow keys for moving.
    Space or LMB for shooting.
    Escape or QUIT for exiting."""
    
    # Global variables that might be changed
    global running
    global end_screen
    global main_char
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            end_screen = False
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
                end_screen = False
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

def populate(constructor):
    """Function for creating a new sprite object at a random location.
    
    `constructor` is the constructor of the object that only accepts one parameter: `board`. Use lambda expression for more complicated constructors."""
    global sprites
    global board
    
    m = constructor(board)
    m.set_board_position(\
        (random.randint(50, board.width-50),\
        random.randint(50, board.height-50)))
    sprites.add(m)
    return m

def spawn_creepy():
    """Spawn a creepy monster with the `main_char` as the target."""
    global main_char
    m = populate(lambda(b): game_object.CreepyMonster(b, main_char))
    monsters.add(m)
    
def spawn_silly():
    """Spawn a silly monster"""
    m = populate(game_object.SillyMonster)
    monsters.add(m)

def spawn_random_monster():
    """Spawn a monster at random. May not spawn any at all (if lucky)."""
    c = random.randint(1,100)
    if c<60:
        spawn_silly()
    elif c<90:
        spawn_creepy()
    else:
        pass    

def create_flower():
    """Spawn a background flower"""
    m = populate(game_object.Background)

def game_over():
    """Game over function: stops the game and updates flag."""
    global running
    global end_screen
    print "GAME OVER!"
    
    running = False
    end_screen = True

def collisions():
    """Resolve all collisions, such as projectile hits."""
    global monsters
    global player_projectiles
    global sprites
    
    #Monster hit by player's projectiles
    for monster in pygame.sprite.groupcollide(monsters, player_projectiles, 0, 1):
        if monster.take_damage(1):
            monsters.remove(monster)
            sprites.remove(monster)
            spawn_random_monster()
            spawn_random_monster()
    
    #Player attacked by monster
    for monster in pygame.sprite.spritecollide(main_char, monsters, 0):
        if main_char.take_damage(monster.attack()):
            game_over()
            return

def remove_terminated_projectiles():
    """Remove projectiles that have been travelling for too long."""
    global sprites
    global player_projectiles
    for p in player_projectiles:
        if p.terminated:
            sprites.remove(p)
            player_projectiles.remove(p)

def init():
    """Spawns flowers and start monsters."""
    spawn_silly()
    spawn_silly()
    spawn_creepy()
    for r in range(8):
        create_flower()

def main():
    """Main function: handles loop and puts everthing together."""
    # Start the game
    global running
    global end_screen
    running = True
    end_screen = False
    
    global sprites
    global main_char
    global board
    
    global WIDTH
    global HEIGHT
    sprites.add(main_char)
    main_char.set_board_position( board.board_position_of( WIDTH/2, HEIGHT/2) )
    
    init()
    
    ###############
    ## Game loop
    while running:
        # Handle logic
        handle_input()
        update()
        collisions()
        remove_terminated_projectiles()
        
        # Draw to the screen
        draw()
        
        # Tick...
        global ticks
        ticks += 1
        clock.tick(UPDATES_PER_SEC)
    
    # Game over
    if end_screen:
        g = game_object.GameOverScreen()
        g.rect.x = (WIDTH - g.rect.width)/2
        g.rect.y = (HEIGHT - g.rect.height)/2
        
        gr = pygame.sprite.Group()
        gr.add(g)
        
        global screen
        sprites.draw(screen)
        gr.draw(screen)
        pygame.display.flip()
        
        while end_screen:
            handle_input()
            clock.tick(UPDATES_PER_SEC)

    pygame.quit()

# Run
main()