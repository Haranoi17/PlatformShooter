from ClientServer.Client import Client
from ClientServer.Constants import *
from Engine.Engine import Engine
from ClientServerGameLogic.GameMessages import *
from Scripts.Input import Input
import threading
import time


class GameClient(Client):
    def __init__(self):
        Client.__init__(self)
        self.running = True
        self.ID = None
        self.GameEngine = Engine()

        # self.connect(("haranoi18.ddns.net", 5050))
        self.connectToLocalHost()
        self.receiveID()

        self.getServerInfoThread = threading.Thread(target=self.getGameStateFromServer, args=())
        self.getServerInfoThread.start()
        self.sendInputThread = threading.Thread(target=self.sendInput, args=())
        self.sendInputThread.start()

        self.updateClient()

    def getGameStateFromServer(self):
        while self.GameEngine.window.isOpen():
            message = self.socket.recv(MESSAGE_SIZE).decode(ENCODING)
            if message:
                message = message.strip(PADDING_CHARACTER)

    def updateClient(self):
        while self.running:
            self.GameEngine.updateClient()

    def sendInput(self):
        isLeftRightSent = False
        while self.running:
            inputMessage = ""
            if (Input.right or Input.left) and not isLeftRightSent:
                if Input.left:
                    inputMessage = PLAYER_ID + self.ID
                    inputMessage += PLAYER_MOVE + LEFT
                elif Input.right:
                    inputMessage = PLAYER_ID + self.ID
                    inputMessage += PLAYER_MOVE + RIGHT
                isLeftRightSent = True
            elif isLeftRightSent and not (Input.right or Input.left):
                inputMessage = PLAYER_ID + self.ID
                inputMessage += PLAYER_MOVE + STOP
                isLeftRightSent = False
            if Input.space:
                inputMessage = PLAYER_ID + self.ID
                inputMessage += PLAYER_JUMP

            if inputMessage:
                self.send(inputMessage)

    def receiveID(self):
        message = self.socket.recv(MESSAGE_SIZE).decode(ENCODING)
        message = message.strip(PADDING_CHARACTER)
        self.ID = message

    def closeClient(self):
        self.getServerInfoThread.join()
        self.sendInputThread.join()
        self.running = False







