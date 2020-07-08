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

    def drawObject(self, Object):
        x = Object.pos.x - Object.width / 2
        y = Object.pos.y - Object.height / 2
        self.surface.blit(Object.image, (x, y))

    def drawText(self, text, pos=Vector()):
        label = self.font.render(str(text), 1, (0, 255, 0))
        self.surface.blit(label, (pos.x, self.height-pos.y))

    def drawHitBox(self, collidable):
        pygame.draw.rect(self.surface, (0, 255, 0), pygame.rect.Rect(collidable.pos.x - collidable.box.x/2,
                                collidable.pos.y - collidable.box.y/2, collidable.box.x, collidable.box.y), 2)

    def update(self):
        self._inputBehaviour()
        self.display.flip()

    def isOpen(self):
        return self.opened

    def close(self):
        self.opened = False

    def getSize(self):
        return self.size

    def _inputBehaviour(self):
        if Input.Esc:
            self.opened = False
