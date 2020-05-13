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
 
import pygame

def deltaTime(start):
    return pygame.time.get_ticks() - start
    
#initialization
window = Window()
player = Player()

collid = Collidable()

img = pygame.image.load("./resources/character.png")

collid.updateCollidable(Vector(200,10))

#main loop
while window.isOpen():
    timerStart = pygame.time.get_ticks()

    Input.checkInputEvents()
    Collidable.distributeCollisios()
    player.update(deltaTime(timerStart))
    window.draw(img, player.pos)
    window.draw(img, collid.pos)
    window.update()
    Collidable.resetCollisions()
    #print("w:{} s:{} a:{} d:{}".format(Input.up, Input.down, Input.left, Input.right))

#arek chuj