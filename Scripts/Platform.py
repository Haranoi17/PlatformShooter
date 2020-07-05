from Scripts.Object import Object
from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable

class Platform(Object, Collidable):
    def __init__(self, pos):
        Object.__init__(self)
        self.loadImage("./resources/World/platform-placeholder.png")
        Collidable.__init__(self, box=Vector(self.width, self.height))
        self.updateCollidable(pos)


    def update(self):
        self.updateCollidable(self.pos)