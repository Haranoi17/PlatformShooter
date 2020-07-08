from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable

from pygame import image


class Object:
    def __init__(self):
        self.image = None
        self.width = 0
        self.height = 0

    def loadImage(self, path):
        self.image = image.load(path)
        self.width, self.height = self.image.get_size()
