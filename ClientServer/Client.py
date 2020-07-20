import socket
from ClientServer.Constants import *


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address=()):
        self.socket.connect(address)

    def disconnect(self):
        self.send(DISCONNECT_MESSAGE)

    def send(self, message=""):
        if len(message) > MESSAGE_SIZE:
            print("Too big message. Sending terminated.")
            return False

        if len(message) < MESSAGE_SIZE:
            paddingSize = MESSAGE_SIZE - len(message)
            message += PADDING_CHARACTER * paddingSize

        self.socket.send(message.encode(ENCODING))
        return True

    def receive(self):
        message = self.socket.recv(MESSAGE_SIZE).decode(ENCODING)
        print(message)

