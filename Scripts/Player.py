from Scripts.Vector import Vector
from Scripts.CollisionSystem import Collidable
from Scripts.Input import Input
from Scripts.Entity import Entity
from Scripts.Platform import Platform
from Scripts.Gun import Gun
from Scripts.Bullet import Bullet
from Scripts.Animation import Animation
from Scripts.Window import Window
import random
import math
import pygame


class Player(Entity, Collidable, Animation):
    """Python predefined class functions"""

    def __init__(self):
        Entity.__init__(self)
        self.imageOffset = Vector(20, -20)
        Animation.__init__(self, "./resources/Animations/Knight/")
        self.width = self.getImageSize().x
        self.height = self.getImageSize().y
        Collidable.__init__(self, box=Vector(self.width - 90, self.height - 70))
        self.jumpTime = 0
        self.jumping = False
        self.falling = True
        self.rising = False
        self.standing = False
        self.attacking = False
        self.moveDir = Vector()
        self.fallTime = 0
        self.explicitMoveAllowed = True
        self.prevPos = self.pos
        self.gun = Gun()

    """Protected Functions"""

    def _attack(self):
        if Input.mouseLeft:
            self.attacking = True
            self.gun.shoot(self.pos, self, self._calculateMouseRelativePosition())

    def _calculateMoveDirection(self):
        """Returns normalized move direction vector according to buttons pressed"""
        self.moveDir = Vector()

        if Input.left and self.explicitMoveAllowed:
            self.moveDir = self.moveDir + Vector(-1, 0)

        if Input.right and self.explicitMoveAllowed:
            self.moveDir = self.moveDir + Vector(1, 0)

        if Input.space and self.collisionInfo["Bottom"] and self.explicitMoveAllowed:
            self.moveDir = self.moveDir + Vector(0, -1)
            self.jumping = True

        self.moveDir = self.moveDir.normalized()

    def _calculateMouseRelativePosition(self):
        """Returns normalized direction from character towards mouse cursor"""
        relativeMousePos = Vector(Input.mousePos.x - self.pos.x, Input.mousePos.y - self.pos.y)
        return relativeMousePos.normalized()

    def _jump(self, deltaTime, gravity):
        if self.jumping:
            self.explicitMoveAllowed = True
            self.jumpTime += deltaTime
            self.pos.y -= 2.5 - gravity * self.jumpTime ** 2

    def _fall(self, deltaTime, gravity):
        if not self.collisionInfo["Bottom"]:
            self.explicitMoveAllowed = True
            self.fallTime += deltaTime
            self.pos.y += 0.5 + gravity * self.fallTime ** 2

    def _isRising(self):
        self.rising = True if self.prevPos.y > self.pos.y else False

    def _isFalling(self):
        self.falling = True if self.prevPos.y < self.pos.y else False

    def _collisionBehaviourDependingOnTypesOfObjects(self, other):
        if isinstance(other, Platform):
            self.explicitMoveAllowed = True
            if self.collisionInfo["Bottom"] and not self.rising:
                self.falling = False
                self.jumping = False
                self.fallTime = 0
                self.jumpTime = 0
                self.standing = True
            else:
                self.standing = False
        else:
            self.explicitMoveAllowed = False

        if isinstance(other, Bullet) and not other.playerImmune == self:
            self.explicitMoveAllowed = True
            self.getDamage(other.dmg)
            Bullet.remove(other)

    def _animationLogic(self):
        if not self.attacking:
            if self.jumping and self.currentAnimation is not self.animationBase["Jump"]:
                self.frameDelay = 100
                self._changeCurrentAnimation("Jump")
            elif self.standing and self.currentAnimation != self.animationBase["Walk"] and self.moveDir.x:
                self.frameDelay = 100
                self._changeCurrentAnimation("Walk")
            elif self.standing and self.currentAnimation is not self.animationBase["Idle"] and not self.moveDir.x:
                self.frameDelay = 200
                self._changeCurrentAnimation("Idle")

        if self.attacking and self.currentAnimation is not self.animationBase["Attack"]:
            self.frameDelay = 50
            self._changeCurrentAnimation("Attack")

        if self.attacking and self.imageIndex == len(self.animationBase["Attack"]):
            self.attacking = False
        if self.currentAnimation is self.animationBase["Walk"] and self.imageIndex == len(self.animationBase["Walk"])-1:
            self.imageIndex = 2
        if self.currentAnimation is self.animationBase["Jump"] and self.imageIndex == len(self.animationBase["Jump"])-1:
            self.imageIndex = len(self.animationBase["Jump"])-2


    def _shouldFlipImage(self):

        if not self.attacking:
            if self._calculateMouseRelativePosition().x < 0 and not self.flipped:
                self.flipped = True
            if self._calculateMouseRelativePosition().x > 0 and self.flipped:
                self.flipped = False

            if self.moveDir.x < 0 and not self.flipped:
                self.flipped = True
            if self.moveDir.x > 0 and self.flipped:
                self.flipped = False

        self.prevFlipped = self.flipped
        self.flipTrigger = True if self.prevFlipped is not self.flipped else False

    def _setImageOffset(self):
        self.imageOffset = Vector(-20, -20) if self.flipped else Vector(20, -20)

    """Public functions"""

    def update(self, deltaTime, gravity):

        self.updateCollidable(self.pos)
        self._calculateMoveDirection()
        # prevPos has to be written after rising and falling
        self._jump(deltaTime, gravity)
        self._fall(deltaTime, gravity)
        self._isFalling()
        self._isRising()

        self._animationLogic()
        self.animate()

        self.prevPos = self.pos

        self._attack()

        if self.pos.y > Window.height:
            self.pos.y = -self.height
        if self.pos.x < -self.width:
            self.pos.x = Window.width
        if self.pos.x > Window.width:
            self.pos.x = -self.width

        self._move(deltaTime, self.moveDir)
