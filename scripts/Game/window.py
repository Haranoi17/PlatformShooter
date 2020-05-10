import pygame

class window:
    def __init__(self):
        self.opened = True
        self.background_color = (255,255,255)
        self.size = (600, 400)
        window_handle = pygame.display.set_mode(self.size)
    
    def isOpen(self):
        return self.opened

    def close(self):
        self.opened = False