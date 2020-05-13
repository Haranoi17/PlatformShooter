#Exiting when script is run by other script
if __name__ != "__main__":
    print("Run this script directly! (exiting)")
    exit()

from GameScripts.Window import Window
from GameScripts.Vector import Vector
from GameScripts.CollisionSystem import *
from GameScripts.Player import *
from GameScripts.ShootingMechanics import *
from GameScripts.Enemy import *
from GameScripts.Input import *

import os
import pygame

def deltaTime(start):
    return pygame.time.get_ticks() - start
    
clock = pygame.time.Clock()

#initialization
window = Window()
player = Player()

collid = Collidable()


walkRight = [pygame.image.load(pygame.path.join('resources/Game', 'R1.png')), 
        pygame.image.load(pygame.path.join('resources/Game', 'R2.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'R3.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'R4.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'R5.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'R6.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'R7.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'R8.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'R9.png'))]

walkLeftt = [pygame.image.load(pygame.path.join('resources/Game', 'L1.png')), 
        pygame.image.load(pygame.path.join('resources/Game', 'L2.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'L3.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'L4.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'L5.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'L6.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'L7.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'L8.png')),
        pygame.image.load(pygame.path.join('resources/Game', 'L9.png'))]

walkCount = 0

bg = pygame.image.load(pygame.path.join('resources/Game', 'bg.png'))
char = pygame.image.load(pygame.path.join('resources/Game', 'standing.png'))

Window.surface.blit(bg, (0,0))

if walkCount + 1 >= 27: 
    walkCount = 0
if Input.left:
    Window.surface.blit(walkLeftt[walkCount//3], (player.pos))
    walkCount += 1
# dzielone przez 3 bo 9 obrazków mamy 
elif Input.right:
    Window.surface.blit(walkRight[walkCount//3], (player.pos))
    walkCount += 1
else:
    Window.surface.blit(char, (player.pos))

pygame.display.update()

collid.updateCollidable(Vector(200,10))

#main loop
while window.isOpen():
    clock.tick(27) #27 klatek na sekunde 
    timerStart = pygame.time.get_ticks()

    Input.checkInputEvents()
    Collidable.distributeCollisios()
    player.update(deltaTime(timerStart))
    window.draw(char, player.pos)
    window.draw(char, collid.pos)
    window.update()
    Collidable.resetCollisions()
    #print("w:{} s:{} a:{} d:{}".format(Input.up, Input.down, Input.left, Input.right))

#arek chuj