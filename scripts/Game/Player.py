import pygame
import math
import random
from pygame.locals import *
W, H = 800, 700

pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('fajna gjera')

img = pygame.image.load('gaming.png')

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            
def pause():
    while True:
        events()
        k = pygame.key.get_pressed()
        if k[K_F1]: 
            break

class Player:
    def __init__(self, velocity, maxJumpRange):
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange

    def set_location(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True

    def keys(self):
        k = pygame.key.get_pressed()

        if k[K_LEFT]:
            self.xVelocity =- self.velocity
        elif k[K_RIGHT]:
            self.xVelocity = self.velocity
        else:
            self.xVelocity = 0
        if k[K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0
        
    def move(self):
        self.x += self.xVelocity
        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter +=1
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            if self.y <= H - 10 and self.y + self.velocity >= H-10:
                self.y = H - 10
                self.falling = False
            else:
                self.y += self.velocity

    def draw(self, screen):
        screen.blit(img, (self.x, self.y))
        

    def do(self):
        self.keys()
        self.move()
        self.draw()

