from Scripts.CollisionSystem import Collidable
from Scripts.Object import Object
from Scripts.Vector import Vector


class Bullet(Object, Collidable):
    """Static members"""
    bullets = []

    """Python predefined class functions"""
    def __init__(self, moveDir, playerImmune, pos):
        Object.__init__(self)
        Collidable.__init__(self, pos)
        self.playerImmune = playerImmune
        self.flySpeed = 0.1
        self.dmg = 5
        self.moveDir = moveDir
        self.box = Vector(10, 10)
        self.loadImage("./resources/Bullets/bullet.png")
        Bullet.bullets.append(self)

    """Static functions"""
    @classmethod
    def removeOutOfBorder(cls, windowSize=Vector()):
        for bullet in cls.bullets:
            if windowSize.x < bullet.pos.x or bullet.pos.x < 0 or windowSize.y < bullet.pos.y or bullet.pos.y < 0:
                cls.remove(bullet)

    @classmethod
    def remove(cls, bullet):
        Collidable.remove(bullet)
        cls.bullets.remove(bullet)

    """Public functions"""
    def update(self, deltaTime):
        self.pos += self.moveDir * deltaTime * self.flySpeed
        self.updateCollidable(self.pos)

