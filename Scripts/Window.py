import pygame
from Scripts.Input import Input
from Scripts.Vector import Vector


class Window:
    def __init__(self):
        self.opened = True
        self.background_color = (255, 255, 255)
        self.width = 1280
        self.height = 720
        self.size = Vector(self.width, self.height)
        self.display = pygame.display
        self.surface = self.display.set_mode((self.size.x, self.size.y))
        self.font = pygame.font.SysFont("Comic Sans MS", 30)

    def drawEntity(self, entity):
        x = entity.pos.x - entity.width/2
        y = entity.pos.y - entity.height/2
        self.surface.blit(entity.image, (x, y))

    def drawObject(self, object):
        x = object.pos.x - object.width / 2
        y = object.pos.y - object.height / 2
        self.surface.blit(object.image, (x, y))

    def drawText(self, text):
        label = self.font.render("FPS: " + str(int(text)), 1, (0, 255, 0))
        self.surface.blit(label, (40, self.height-40))

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
