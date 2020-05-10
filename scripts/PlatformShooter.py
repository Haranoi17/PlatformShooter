#Exiting when script is run by other script
if __name__ != "__main__":
    print("Run this script directly! (exiting)")
    exit()

from Game.window import *
from Game.CollisionSystem import *
from Game.Player import *
from Game.ShootingMechanics import *
from Game.Enemy import *
import pygame
from pygame.locals import *

pygame.init()
win = window()

while win.isOpen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win.close()