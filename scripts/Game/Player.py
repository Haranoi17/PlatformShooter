from Game.CollisionSystem import Collidable
from Game.Vector import Vector
from Game.Input import Input

class Player(Collidable):
    def __init__(self):
        self.pos = Vector()

    def move(self):
        if Input.right:
            self.pos.x += 1