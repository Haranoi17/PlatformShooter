from ClientServerGameLogic.GameServer import GameServer
import threading


#Exiting when script is run by other script
if __name__ != "__main__":
    print("Run this script directly! (exiting)")
    exit()

server = GameServer()

