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
            return

        if len(message) < MESSAGE_SIZE:
            paddingSize = MESSAGE_SIZE - len(message)
            message += " " * paddingSize

        self.socket.send(message.encode(ENCODING))

    def receive(self):
        message = self.socket.recv(MESSAGE_SIZE).decode(ENCODING)
        print(message)

client = Client()

client.connect((socket.gethostbyname(socket.gethostname()), 5050))

client.send("Za duza wiadomosc -----------------------------------------------------------------------------------------------------------------------------")

client.receive()

client.disconnect()
