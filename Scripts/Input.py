import pygame
from Scripts.Vector import Vector


class Input:
    """Static members"""
    up = False
    down = False
    left = False
    right = False
    space = False
    mouseLeft = False
    mouseRight = False
    mousePos = Vector()
    Num1 = False
    Num2 = False
    Num3 = False
    Esc = False

    """Static functions"""

    @classmethod
    def updateMousePosition(cls):
        mousePosX, mousePosY = pygame.mouse.get_pos()
        cls.mousePos = Vector(mousePosX, mousePosY)

    @classmethod
    def checkInputEvents(cls):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                cls.Esc = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cls.up = True

                if event.key == pygame.K_s:
                    cls.down = True

                if event.key == pygame.K_a:
                    cls.left = True

                if event.key == pygame.K_d:
                    cls.right = True

                if event.key == pygame.K_SPACE:
                    cls.space = True

                if event.key == pygame.K_1:
                    cls.Num1 = True

                if event.key == pygame.K_2:
                    cls.Num2 = True

                if event.key == pygame.K_ESCAPE:
                    cls.Esc = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    cls.up = False

                if event.key == pygame.K_s:
                    cls.down = False

                if event.key == pygame.K_a:
                    cls.left = False

                if event.key == pygame.K_d:
                    cls.right = False

                if event.key == pygame.K_SPACE:
                    cls.space = False

                if event.key == pygame.K_1:
                    cls.Num1 = False

                if event.key == pygame.K_2:
                    cls.Num2 = False

                if event.key == pygame.K_ESCAPE:
                    cls.Esc = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    cls.mouseLeft = True

                if event.button == pygame.BUTTON_RIGHT:
                    cls.mouseRight = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    cls.mouseLeft = False

                if event.button == pygame.BUTTON_RIGHT:
                    cls.mouseRight = False
