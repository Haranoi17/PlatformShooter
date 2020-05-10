from Game.Vector import *

class Collidable:
    collidables = []

    def __init__(self):
        self.pos = Vector()
        self.box = Vector()
        self.left
        self.right
        self.top
        self.bottom
        Collidable.collidables.append(self)

    def updateSides(self):
        self.left    = self.pos.x - self.box.x
        self.right   = self.pos.x + self.box.x
        self.top     = self.pos.y + self.box.y
        self.bottom  = self.pos.y - self.box.y
    
    #Checks if collision occured and sends information which side has collided
    def collisionCheck(self, other):
        if self.right > other.left and self.right < other.right:
            print("zajebał z prawej")
        
        if self.left > other.left and self.left < other.right:
            print("zajebał z lewej")

        if self.top > other.bottom and self.top < other.top:
            print("zajebał łbem")
        
        if self.bottom > other.bottom and self.bottom < other.top:
            print("stoi chłop")

    @classmethod
    #This function iterates through all collidable objects and check for collision
    def distributeCollisios(cls):
        for i in range(len(cls.collidables) - 1):
            j = i + 1
            while j < len(cls.collidables):
                cls.collidables[i].collisionCheck(cls.collidables[j])
            

        


