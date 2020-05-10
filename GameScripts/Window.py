import pygame
from GameScripts.Input import Input
from GameScripts.Vector import Vector

class Window:
    def __init__(self):
        self.opened = True
        self.background_color = (255, 255, 255)
        self.size = Vector(600, 400)
        self.display = pygame.display
        self.surface = self.display.set_mode((self.size.x, self.size.y))

    def draw(self, image, pos):
        self.surface.blit(image, (pos.x, pos.y))

    def update(self):
        self.inputBehaviour()
        self.display.flip()

    def isOpen(self):
        return self.opened

    def close(self):
        self.opened = False

    def inputBehaviour(self):
        if Input.Esc == True:
            self.opened = False
