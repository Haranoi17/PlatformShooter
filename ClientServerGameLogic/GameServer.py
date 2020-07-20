from ClientServer.Server import Server
from Engine.Engine import Engine


class GameServer(Server):
    def __init__(self):
        Server.__init__(self)
        self.GameEngine = Engine()

    def startGameLogic(self):

