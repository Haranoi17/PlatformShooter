import pygame
from Scripts.Input import Input
from Scripts.Vector import Vector


class Window:
    def __init__(self):
        self.opened = True
        self.background_color = (255, 255, 255)
        self.size = Vector(1280, 720)
        self.display = pygame.display
        self.surface = self.display.set_mode((self.size.x, self.size.y))

    def drawEntity(self, entity):
        x = entity.pos.x - entity.width/2
        y = entity.pos.y - entity.height/2
        self.surface.blit(entity.image, (x, y))

    def drawObject(self, object):
        x = object.pos.x - object.width / 2
        y = object.pos.y - object.height / 2
        self.surface.blit(object.image, (x, y))

    def drawHitBox(self, entity):
        pygame.draw.rect(self.surface, (0, 255, 0), pygame.rect.Rect(entity.pos.x - entity.width/2, entity.pos.y - entity.height/2, entity.width, entity.height), 2)

    def update(self):
        self._inputBehaviour()
        self.display.flip()

    def isOpen(self):
        return self.opened

    def close(self):
        self.opened = False

    def _inputBehaviour(self):
        if Input.Esc:
            self.opened = False
