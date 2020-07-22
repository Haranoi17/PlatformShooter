from ClientServer.Server import Server
from ClientServer.Constants import *
from ClientServerGameLogic.GameMessages import *
from Scripts.Vector import Vector
from Engine.Engine import Engine
import threading
import time


class GameServer(Server):
    GameEngine = Engine(hasWindow=True)
    def __init__(self):
        Server.__init__(self)

        self.isRunning = True
        self.activeConnectionsData = []
        self.availableIDs = {str(x): True for x in range(0, 10)}

        self.listen()

        self.connectionThread = threading.Thread(target=self.accept, args=())
        self.connectionThread.start()

        self.updateGameLogic()
        # self.connectionThread = threading.Thread(target=GameServer.serverLoop, args=(self,))

    def updateGameLogic(self):
        self.GameEngine.updateServer()
        #self.sendGameState()

    def sendGameState(self):
        for client in self.activeConnectionsData:
            conn, addr = client
            conn.send("H".encode(ENCODING))

    def handleClient(self, conn, addr) -> None:
        connected = True
        connectionData = (conn, addr)
        self.activeConnectionsData.append(connectionData)
        clientID = self.pickID()
        self.GameEngine.registerPlayer(clientID)
        self.sendToClient(conn, clientID)

        while connected:
            message = self.receive(conn)
            if message:
                message = message.strip(PADDING_CHARACTER)
                connected = self.handleMessage(message)
                print(message)

        self.activeConnectionsData.remove(connectionData)
        self.releaseID(clientID)
        conn.close()

    def pickID(self) -> str:
        newID = None
        print("picking")
        for key in self.availableIDs.keys():
            if self.availableIDs[key]:
                newID = key
                self.availableIDs[key] = False
                break
        return newID

    def releaseID(self, key):
        self.availableIDs[key] = True

    def handleMessage(self, message) -> bool:
        """Returns True if connection is still up and False when connetion is getting closed"""
        idIndex = message.find(PLAYER_ID) + len(PLAYER_ID)
        ID = message[idIndex]  # string

        if DISCONNECT_MESSAGE in message:
            return False

        if PLAYER_MOVE in message:
            moveValueIndex = message.find(PLAYER_MOVE) + len(PLAYER_MOVE)
            moveDir = Vector(1, 0) if message[moveValueIndex] == RIGHT else Vector(-1, 0)
            self.GameEngine.movePlayer(ID, moveDir)

        return True

    def closeServer(self):
        self.gameLogicThread.join()
        print("Terminating server")
        exit()
