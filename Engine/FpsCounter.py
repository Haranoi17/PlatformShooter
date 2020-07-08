import pygame


class FpsCounter:
    def __init__(self, freq):
        self.frames = 0
        self.startTime = pygame.time.get_ticks()
        self.stopTime = 0
        self.elapsedTime = 0
        self.freq = freq
        self.fps = 0

    def measureTime(self):
        self.stopTime = pygame.time.get_ticks()
        self.elapsedTime = self.stopTime - self.startTime

    def countFPS(self):
        if self.elapsedTime > self.freq:
            self.fps = self.frames / (self.elapsedTime / 1000)
            self._reset()

    def enable(self):
        self.addFrame()
        self.measureTime()
        self.countFPS()

    def addFrame(self):
        self.frames += 1

    def _reset(self):
        self.frames = 0
        self.elapsedTime = 0
        self.startTime = self.stopTime

    def __str__(self):
        return f"FPS: {int(self.fps)}"
