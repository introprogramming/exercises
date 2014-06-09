import random

class TetrisObject:
    """A TetrisObject represents the actual object that the player
    can control. It consists of four blocks (positioned depending on
    the shape) and can move down, to the sides or be rotated."""
    
    # Actual position
    x = 3;
    y = 0;
    
    # The current state of rotation
    rotation = 0;
    
    # The constructor, randomly picks on of the possible shapes
    def __init__(self):
        rand = random.randint(0,6)
        
        # Every shape has a series of possible rotations and a color
        if rand == 0:
            # J-shape
            self.shape = (((0,1),(1,1),(2,1),(2,2)),
                          ((1,0),(1,1),(1,2),(0,2)),
                          ((0,0),(0,1),(1,1),(2,1)),
                          ((2,0),(1,0),(1,1),(1,2)))
            self.color = (0, 255, 0)
        elif rand == 1:
            # L-shape
            self.shape = (((0,2),(0,1),(1,1),(2,1)),
                          ((0,0),(1,0),(1,1),(1,2)),
                          ((0,1),(1,1),(2,1),(2,0)),
                          ((1,0),(1,1),(1,2),(2,2)))
            self.color = (0, 0, 255)
        elif rand == 2:
            # S-shape
            self.shape = (((0,2),(1,2),(1,1),(2,1)),
                          ((1,0),(1,1),(2,1),(2,2)))
            self.color = (0, 255, 255)
        elif rand == 3:
            # T-shape
            self.shape = (((0,1),(1,1),(1,2),(2,1)),
                          ((1,0),(1,1),(0,1),(1,2)),
                          ((0,1),(1,1),(1,0),(2,1)),
                          ((1,0),(1,1),(2,1),(1,2)))
            self.color = (255, 255, 0)
        elif rand == 4:
            # Z-shape
            self.shape = (((0,1),(1,1),(1,2),(2,2)),
                          ((1,2),(1,1),(2,1),(2,0)))
            self.color = (255, 0, 255)
        elif rand == 5:
            # |-shape
            self.shape = (((0,2),(1,2),(2,2),(3,2)),
                          ((2,0),(2,1),(2,2),(2,3)))
            self.color = (128, 128, 128)
        elif rand == 6:
            # box-shape
            self.shape = (((1,1),(1,2),(2,1),(2,2)),
                          ((1,1),(1,2),(2,1),(2,2)))
            self.color = (0, 0, 0)
        
    def get_pos(self):
        """Returns a tuple of the position of the shape's 4 blocks"""
    
        return ((self.shape[self.rotation][0][0] + self.x, self.shape[self.rotation][0][1] + self.y),
                (self.shape[self.rotation][1][0] + self.x, self.shape[self.rotation][1][1] + self.y),
                (self.shape[self.rotation][2][0] + self.x, self.shape[self.rotation][2][1] + self.y),
                (self.shape[self.rotation][3][0] + self.x, self.shape[self.rotation][3][1] + self.y))
        
    def rotate(self, blocks):
        """Rotates the shape of this object if the resulting
        shape after rotation is at a valid position."""
        
        
        new_shape = self.shape[(self.rotation + 1) % len(self.shape)]
        
        for i in range(len(new_shape)):
            if new_shape[i][0] + self.x < 0 or new_shape[i][1] + self.x >= len(blocks[0]) or blocks[new_shape[i][1] + self.y][new_shape[i][0] + self.x]:
                return
                
        self.rotation = (self.rotation + 1) % len(self.shape)
            
    def move_x(self, dx, blocks):
        """Moves this object to the left (negative dx),
        or to the right (positive dx) if possible"""
        
        # If the new position won't be valid set dx to 0
        for i in range(len(self.shape[self.rotation])):
            if self.get_pos()[i][0] + dx < 0 or self.get_pos()[i][0] + dx >= len(blocks[0]) or blocks[self.get_pos()[i][1]][self.get_pos()[i][0] + dx]:
                dx = 0
        
        # Update the position
        self.x += dx
            
    def move_y(self, blocks):
        """Moves this object downwards if possible.
        Returns True if it was successfully moved,
        False otherwise"""
        
        # If the new position is not valid, return False
        for i in range(len(self.shape[self.rotation])):
            if self.get_pos()[i][1] + 1 >= len(blocks) or blocks[self.get_pos()[i][1]+ 1][self.get_pos()[i][0]]:
                return False
                
        # Update the position and return True when finished
        self.y += 1
        return True
