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
        self.loadMark = None
        self.players = []

        self._buildPlatforms()

    """Protected functions"""
    def _buildPlatforms(self):
        for i in range(20):
            self.platforms.append(Platform(Vector(100, 200)))

    def _checkSaveAgreement(self, filename):
        if filename in os.listdir("./resources/World"):
            choice = input("This file already exists. Proceed? (y/n): ")
            self.canWrite = True if choice == "y" else False

    def _saveWorldToFile(self, filename):
        self._checkSaveAgreement(filename)
        if self.canWrite:
            with open(os.path.join(self.worldsPath, filename), "w") as file:
                print("saving platforms")
                file.write("Platforms\n")

                for platform in self.platforms:
                    file.write(f"{platform.pos.x} {platform.pos.y}\n")

                file.write("End")
                print("Successfully saved world!")
        else:
            print(f"No agreement on writing to file named: {filename}")

    def _readWorldFromFile(self, filename):
        with open(os.path.join(self.worldsPath, filename), "r") as file:
            print("Destroying current world")
            self._clearWorld()

            print("World loading")
            for line in file.readlines():
                if self._checkMark(line):
                    continue

                if "Platforms" in self.loadMark:
                    posX = float(line.split(" ")[0])
                    posY = float(line.split(" ")[1])
                    self.platforms.append(Platform(pos=Vector(posX, posY)))
            print("World Loaded!")

    def _checkMark(self, line=str()):
        """Returns True to indicate that mark is in current line and lets us skip one line to data of given object"""
        if "Platforms" in line:
            self.loadMark = "Platforms"
            return True
        elif "End" in line:
            self.loadMark = "End"
            return True
        else:
            return False


    def _removeAllPlatforms(self):
        for platform in self.platforms:
            Collidable.remove(platform)
        self.platforms.clear()

    def _clearWorld(self):
        self._removeAllPlatforms()

    """Public functions"""
    def saveWorld(self):
        filename = input("Name your world: ")
        self._saveWorldToFile(filename)

    def loadWorld(self):
        os.listdir(self.worldsPath)
        filename = input("Choose world to load: ")
        self._readWorldFromFile(filename)
