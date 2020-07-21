from ClientServerGameLogic.GameClient import GameClient


#Exiting when script is run by other script
if __name__ != "__main__":
    print("Run this script directly! (exiting)")
    exit()

client = GameClient()
