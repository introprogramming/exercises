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
            self.shape = (((0,1),(1,1),(2,1),(2,2)),
                          ((1,0),(1,1),(1,2),(0,2)),
                          ((0,0),(0,1),(1,1),(2,1)),
                          ((2,0),(1,0),(1,1),(1,2)))
            self.color = (0, 255, 0)
        elif rand == 1:
            self.shape = (((0,2),(0,1),(1,1),(2,1)),
                          ((0,0),(1,0),(1,1),(1,2)),
                          ((0,1),(1,1),(2,1),(2,0)),
                          ((1,0),(1,1),(1,2),(2,2)))
            self.color = (0, 0, 255)
        elif rand == 2:
            self.shape = (((0,2),(1,2),(1,1),(2,1)),
                          ((1,0),(1,1),(2,1),(2,2)))
            self.color = (0, 255, 255)
        elif rand == 3:
            self.shape = (((0,1),(1,1),(1,2),(2,1)),
                          ((1,0),(1,1),(0,1),(1,2)),
                          ((0,1),(1,1),(1,0),(2,1)),
                          ((1,0),(1,1),(2,1),(1,2)))
            self.color = (255, 255, 0)
        elif rand == 4:
            self.shape = (((0,1),(1,1),(1,2),(2,2)),
                          ((1,2),(1,1),(2,1),(2,0)))
            self.color = (255, 0, 255)
        elif rand == 5:
            self.shape = (((0,2),(1,2),(2,2),(3,2)),
                          ((2,0),(2,1),(2,2),(2,3)))
            self.color = (128, 128, 128)
        elif rand == 6:
            self.shape = (((1,1),(1,2),(2,1),(2,2)),
                          ((1,1),(1,2),(2,1),(2,2)))
            self.color = (0, 0, 0)
        
    def getPos(self):
        """Returns a tuple of the position of the shape's 4 blocks"""
    
        return ((self.shape[self.rotation][0][0] + self.x, self.shape[self.rotation][0][1] + self.y),
                (self.shape[self.rotation][1][0] + self.x, self.shape[self.rotation][1][1] + self.y),
                (self.shape[self.rotation][2][0] + self.x, self.shape[self.rotation][2][1] + self.y),
                (self.shape[self.rotation][3][0] + self.x, self.shape[self.rotation][3][1] + self.y))
        
    def rotate(self, blocks):
        """Rotates the shape of this object if the resulting
        shape after rotation is at a valid position."""
        
        
        newShape = self.shape[(self.rotation + 1) % len(self.shape)]
        
        for i in range(len(newShape)):
            if newShape[i][0] + self.x < 0 or newShape[i][1] + self.x >= len(blocks[0]) or blocks[newShape[i][1] + self.y][newShape[i][0] + self.x]:
                return
                
        self.rotation = (self.rotation + 1) % len(self.shape)
            
    def moveX(self, dx, blocks):
        """Moves this object to the left (negative dx),
        or to the right (positive dx) if possible"""
        
        # If the new position won't be valid set dx to 0
        for i in range(len(self.shape[self.rotation])):
            if self.getPos()[i][0] + dx < 0 or self.getPos()[i][0] + dx >= len(blocks[0]) or blocks[self.getPos()[i][1]][self.getPos()[i][0] + dx]:
                dx = 0
        
        # Update the position
        self.x += dx
            
    def moveY(self, blocks):
        """Moves this object downwards if possible.
        Returns True if it was successfully moved,
        False otherwise"""
        
        # If the new position is not valid, return False
        for i in range(len(self.shape[self.rotation])):
            if self.getPos()[i][1] + 1 >= len(blocks) or blocks[self.getPos()[i][1]+ 1][self.getPos()[i][0]]:
                return False
                
        # Update the position and return True when finished
        self.y += 1
        return True
