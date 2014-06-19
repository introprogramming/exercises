
import pygame, os.path, math

main_dir = os.path.split(os.path.abspath(__file__))[0]
resource_path = main_dir+os.path.sep+"resources"+os.path.sep

def norm(x, y):
    return math.sqrt(x**2 + y**2)

def vector_to(speed, from_x, from_y, target_x, target_y):
    x = target_x - from_x
    y = target_y - from_y
    
    return (x*speed/norm(x,y), y*speed/norm(x,y))

class Board:
    def __init__(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
        self.width = 1200
        self.height = 1200
        self.screen_x = (self.width - win_width)/2
        self.screen_y = (self.height - win_height)/2
        
        self.limit_x = win_width/2
        self.limit_y = win_height/2
    
    def graph_position_of(self, board_x, board_y):
        x = board_x - self.screen_x
        y = board_y - self.screen_y
        return (x, y)
    
    def set_screen_position(self, board_x, board_y):
        self.screen_x = board_x - self.win_width/2
        self.screen_y = board_y - self.win_height/2
        #TODO fix
        if self.screen_x < 0:
            self.screen_x = 0
        elif self.screen_x + self.win_width > self.width:
            self.screen_x = self.width - self.win_width
        
        if self.screen_y < 0:
            self.screen_y = 0
        elif self.screen_y + self.win_height > self.height:
            self.screen_y = self.height - self.win_height
    
    def board_position_of(self, graph_x, graph_y):
        return (self.screen_x + graph_x, self.screen_y + graph_y)
    
class GraphObject(pygame.sprite.Sprite):
    
    def __init__(self, image, board):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.vx = 0
        self.vy = 0
        self.board_x = 0
        self.board_y = 0
        self.board = board
        self.update(0)
    
    def set_board_position(self, board_p):
        (self.board_x, self.board_y) = board_p
        self.update(0)
    
    #def set_screen_position(self, x, y):
    #    self.rect.x = x
    #    self.rect.y = y
    
    def check(self):
        if self.board_x < 0:
            self.board_x = 0
        elif self.board_x + self.rect.width > self.board.width:
            self.board_x = self.board.width - self.rect.width
        
        if self.board_y < 0:
            self.board_y = 0
        elif self.board_y + self.rect.height > self.board.height:
            self.board_y = self.board.height - self.rect.height
    
    def update(self, time):
        self.board_x = (time*self.vx + self.board_x)
        self.board_y = (time*self.vy + self.board_y)
        self.check()
        (self.rect.x, self.rect.y) = self.board.graph_position_of(self.board_x, self.board_y)

class Character(GraphObject):
    
    image = pygame.image.load(resource_path+"character.png")
    speed = 100
    
    def __init__(self, board):
        GraphObject.__init__(self, Character.image.convert(), board)
        self.horizontal_dir = 0
        self.vertical_dir = 0
        
    
    def stop(self, xdir, ydir):
        if self.horizontal_dir == xdir:
            self.horizontal_dir = 0
        
        if self.vertical_dir == ydir:
            self.vertical_dir = 0
        
        self.fix_speed()
    
    def move(self, xdir, ydir):
        if xdir != 0:
            self.horizontal_dir = xdir
        
        if ydir  != 0:
            self.vertical_dir = ydir
        
        self.fix_speed()
        
    def fix_speed(self):
        if self.horizontal_dir == 0 and self.vertical_dir == 0:
            self.vx = 0
            self.vy = 0
        else :
            (self.vx, self.vy) = vector_to(Character.speed, 0, 0, self.horizontal_dir, self.vertical_dir)
    
class Projectile(GraphObject):
    image = pygame.image.load(resource_path+"projectile.png")
    speed = 500
    max_time = 2
    
    def __init__(self, board):
        self.time_travelled = 0
        GraphObject.__init__(self, Character.image.convert(), board)
        
    def set_target(self, target_x, target_y):
        (self.vx, self.vy) = vector_to(Projectile.speed, self.rect.x, self.rect.y, target_x, target_y)
        
    def update(self, time):
        GraphObject.update(self, time)
        self.time_travelled = self.time_travelled + time
        if self.time_travelled > Projectile.max_time:
            #TODO
            pass