import socket
import json
import utils
import time
import sys

SERVER_IP   = 'cgi-475508' # 'lshays-VirtualBox' 
PORT_NUMBER = 12345
SIZE = 1024

class Client(object):

    def __init__(self, host=SERVER_IP, port=PORT_NUMBER):
        print "Connecting to server..."
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print "Connection successful"
        self.name = raw_input("Enter Name: ")

    def register(self):
        self.send("REGISTER " + self.name)
        data = self.receive()
        if data == "QUIT":
            print "Server at max player limit"
            self.socket.close()
            return False
        else:
            print "Registered"
            if data[-1] ==  "W":
                print "Waiting on more players to join"
            return True

    def send(self, message):
        self.socket.send(message)

    def receive(self):
        return self.socket.recv(SIZE)
        
    def startGame(self):
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
        
    def getMove(self, response, chips):
        prompt = ""
        currentBet = 0
        extra = ""
        if "BET" in response:
            prompt += "<b> to bet\n"
        if "PASS" in response:
            prompt += "<p> to pass\n"
        if "RAISE" in response:
            prompt += "<r> to raise\n"
        if "FOLD" in response:
            prompt += "<f> to fold\n"
        if "CALL" in response:
            prompt += "<c> to call\n"
        if len(response.split()) > 1:
            currentBet = int(response.split()[1])
        if currentBet:
            extra = "Current Bet: {0}\n".format(currentBet)
        move = raw_input(extra + prompt).lower()
        if move == "b":
            if "BET" not in response:
                print "You can't do that!"
                return self.getMove(response, chips)
            bet = utils.placeBet(chips)
            return "b " + str(bet)
        elif move == "r":
            bet = utils.raiseBet(currentBet, chips)
            if "RAISE" not in response:
                print "You can't do that!"
                return self.getMove(response, chips)
            return "r " + str(bet)
        elif move == "c":
            if "CALL" not in response:
                print "You can't do that!"
                return self.getMove(response, chips)
            return "c " + str(currentBet)
        elif move == "p":
            if "PASS" not in response:
                print "You can't do that!"
                return self.getMove(response, chips)
        elif move == "f":
            if "FOLD" not in response:
                print "You can't do that!"
                return self.getMove(response, chips)
        else:
            print "Invalid move dummy!"
            return self.getMove(response, chips)
        return move
        
    def placeBet(self, chips):
        self.send("FIRSTBET")
        response = self.receive()
        if response == "INACTIVE":
            self.send("GARBAGE")
            self.receive()
            return -1
        if response == "WINNER":
            self.send("GARBAGE")
            self.receive()
            return -69
        move = self.getMove(response, chips)
        self.send(move)
        self.receive()
        if move[0] == 'b':
            return int(move.split()[1])
        if move[0] == 'r':
            return int(move.split()[1])
        if move[0] == 'c':
            return int(move.split()[1])
        return 0
        
    def placeSecondBet(self, chips):
        self.send("SECONDBET")
        response = self.receive()
        if response == "GARBAGE":
            return 0
        else:
            myBet = int(response.split()[2])
            move = self.getMove(response, chips)
            self.send(move)
            if move == 'f':
                return -1
            return int(move.split()[1])-myBet
             
        
    def getPot(self):
        time.sleep(0.25)
        self.send("GETPOT")
        return int(self.receive())
        
    def newGame(self):
        self.send("NEWGAME")
        if self.receive() != "READY":
            print "Something went wrong..."
            sys.exit()
            
