import os
import pygame
from Scripts.Vector import Vector


class Animation:
    def __init__(self, animationPath):
        self.animationBase = {}
        self.animationNames = []
        self.lastFrameTime = 0
        self.imageIndex = 0
        self.frameDelay = 200
        self._load_animations(animationPath)
        self.currentAnimation = self.animationBase["Idle"]
        self.currentImage = self.currentAnimation[self.imageIndex]

    def _load_animations(self, path):
        for animationName in os.listdir(path):
            self.animationBase.update({animationName : []})
            self.animationNames.append(animationName)
            animationPath = os.path.join(path, animationName)

            for imageName in os.listdir(animationPath):
                self.animationBase[animationName].append(pygame.image.load(os.path.join(animationPath, imageName)))

    def getImageSize(self):
        x, y = self.currentImage.get_size()
        return Vector(x, y)

    def changeCurrentAnimation(self, animationName):
        if animationName in self.animationNames:
            self.currentAnimation = self.animationBase[animationName]
            self.imageIndex = 0

    def animate(self):
        if pygame.time.get_ticks() - self.lastFrameTime > self.frameDelay:
            if self.imageIndex < len(self.currentAnimation):
                self.currentImage = self.currentAnimation[self.imageIndex]
                self.imageIndex += 1
            else:
                self.imageIndex = 0
            self.lastFrameTime = pygame.time.get_ticks()

    def printAnimations(self):
        """returns loaded animations names"""
        print(self.animationNames)
