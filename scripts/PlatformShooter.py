#Exiting when script is run by other script
if __name__ != "__main__":
    print("Run this script directly! (exiting)")
    exit()

from Game.Window import *
from Game.CollisionSystem import *
from Game.Player import *
from Game.ShootingMechanics import *
from Game.Enemy import *
from Game.Input import *
import pygame

#initialization
pygame.init()
window = Window()
player = Player()
player2 = Player()

img = pygame.image.load("../resources/0.png")

#main loop
while window.isOpen():
    Input.checkInputEvents()
    Collidable.distributeCollisios()
    #window.handle.fill(0,0,0)
    player.move()
    window.draw(img, player.pos)
    window.update()
    #print("w:{} s:{} a:{} d:{}".format(Input.up, Input.down, Input.left, Input.right))
