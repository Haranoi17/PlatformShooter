import socket
from ClientServer.Constants import *
import threading


class Server:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        print("Server started!")

    def listen(self):
        self.socket.listen()
        print("Listening for connections...")

    def accept(self):
        conn, addr = self.socket.accept()
        print(f"something connected! {addr}")
        thread = threading.Thread(target=Server.handleClient, args=(self, conn, addr))
        thread.start()

    def handleClient(self, conn, addr):
        connected = True
        while connected:
            message = self.receive(conn)
            if message:
                message = message.strip(PADDING_CHARACTER)
                print(f"[{addr}] {message}")
                self.sendToClient(conn, "Data Received")
                if message == DISCONNECT_MESSAGE:
                    print("closing")
                    connected = False
        conn.close()

    def sendToClient(self, connection, message=""):
        if len(message) > MESSAGE_SIZE:
            print("Too big message. Sending terminated.")
            return False

        if len(message) < MESSAGE_SIZE:
            paddingSize = MESSAGE_SIZE - len(message)
            message += " " * paddingSize

        connection.send(message.encode(ENCODING))
        return True

    def receive(self, connection) -> str:
        message = connection.recv(MESSAGE_SIZE).decode(ENCODING)
        return message


server = Server()

server.listen()

server.accept()
