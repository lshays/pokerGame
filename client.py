import socket
import json

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 12345
SIZE = 1024

class Client(object):

    def __init__(self, host, port):
        print "Connecting to server..."
        self.host = host
        self.port = port
        self.registered = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print "Connection successful"
        self.name = raw_input("Enter Name: ")

    def register(self):
        self.send("REGISTER " + self.name)
        if self.receive() != "REGISTERED":
            print "Server at max player limit"
            self.socket.close()
        else:
            self.registered = True

    def send(self, message):
        self.socket.send(message)

    def receive(self):
        return self.socket.recv(SIZE)
        
    def startGame(self):
        self.send("STARTGAME")
        response = self.receive()
        if response == "WAITFORPLAYERS":
            print "Waiting for more players to join"
        while response == "WAITFORPLAYERS":
            self.send("STARTGAME")
            response = self.receive()
            
    def getSharedCards(self):
        self.send("GETSHAREDCARDS")
        response = self.receive()
        response = json.loads(response)
        response = [x.encode('ascii') for x in response]
        return response
        
    def getHand(self):
        self.send("GETHAND")
        response = self.receive()
        response = json.loads(response)
        response = [x.encode('ascii') for x in response]
        return response
        
    def getOtherHands(self):
        self.send("GETOTHERHANDS")
        response = self.receive()
        response = json.loads(response)
        encoded = []
        for hand in response:
            asciiHand = []
            for card in hand:
                asciiHand.append(card.encode('ascii'))
            encoded.append(asciiHand)
        return encoded
        
    def newGame(self):
        self.send("NEWGAME")
