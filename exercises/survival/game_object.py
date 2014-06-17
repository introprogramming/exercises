
import pygame, os.path, math

resource_path = "resources"+os.path.sep

def norm(x, y):
    return math.sqrt(x**2 + y**2)

def vector_to(speed, from_x, from_y, target_x, target_y):
    x = target_x - from_x
    y = target_y - from_y
    
    return (x*speed/norm(x,y), y*speed/norm(x,y))

class GraphObject(pygame.sprite.Sprite):
    board_width = 1200
    board_height = 1200
    
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.vx = 200
        self.vy = 200
        
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def update(self, time):
        print time
        self.rect.x = (time*self.vx + self.rect.x)%GraphObject.board_width
        self.rect.y = (time*self.vy + self.rect.y)%GraphObject.board_height
        print self.rect.x, self.rect.y

class Character(GraphObject):
    
    image = pygame.image.load(resource_path+"character.png")
    
    def __init__(self):
        GraphObject.__init__(self, Character.image.convert())
        
class Projectile(GraphObject):
    image = pygame.image.load(resource_path+"projectile.png")
    speed = 500
    
    def __init__(self):
        GraphObject.__init__(self, Character.image.convert())
        
    def set_target(self, target_x, target_y):
        (self.vx, self.vy) = vector_to(Projectile.speed, self.rect.x, self.rect.y, target_x, target_y)