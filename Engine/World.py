from Scripts.Platform import Platform
from Scripts.Vector import Vector
from Scripts.Player import Player
from Scripts.CollisionSystem import Collidable
import random
import os


class World:
    platforms = []
    """Python predefined class functions"""
    def __init__(self):
        self.worldsPath = "./resources/World/"
        self.canWrite = True
        self.loading = {"Platforms": False, "End": False}
        self.player = Player()
        self._buildPlatforms()

    """Protected functions"""
    def _buildPlatforms(self):
        for i in range(20):
            World.platforms.append(Platform(Vector(random.random() * 1000, random.random() * 600)))


    def _checkSaveAgreement(self, filename):
        if filename in os.listdir("./resources/World"):
            choice = input("This file already exists. Proceed? (y/n): ")
            self.canWrite = True if choice == "y" else False

    def _saveWorldToFile(self, filename):
        self._checkSaveAgreement(filename)
        if self.canWrite:
            with open(os.path.join(self.worldsPath, filename), "w") as file:
                print("saving platforms")
                file.write("Platforms")
                for platform in self.platforms:
                    file.write(f"{platform.pos.x} {platform.pos.y}")

                file.write("End")
        else:
            print(f"No agreement on writing to file named: {filename}")

    def _readWorldFromFile(self, filename):
        with open(os.path.join(self.worldsPath, filename), "r") as file:
            print("World loading")
            for line in file.readline():
                if self._checkMark(line):
                    continue

                if self.loading["Platforms"]:
                    posX = line.split(" ")[0]
                    posY = line.split(" ")[1]
                    self.platforms.append(Platform(pos=Vector(posX, posY)))



    def _checkMark(self, line):
        isThereMark = False
        if line == "Platforms":
            self.loading["Platforms"] = True
            isThereMark = True
        elif line == "End":
            self.loading["Platforms"] = False
            print("Loading ended successfully!")
            isThereMark = True
        return isThereMark


    """Public functions"""
    def saveWorld(self):
        filename = input("Name your world: ")
        self._saveWorldToFile(filename)

    def loadWorld(self):
        os.listdir(self.worldsPath)
        filename = input("Choose world to load: ")
        self._readWorldFromFile(filename)
