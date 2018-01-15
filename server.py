import socket
import threading
import dealer
import barrier
import json

ip = "localhost"
port = 12345
numPlayers = 2

class Player(object):
    def __init__(self, conn, active):
        self.connection = conn
        self.active = active


class ThreadedServer(object):

    def __init__(self, host, port):
        print "Starting poker server..."
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.players = []
        self.currentPlayer = 0
        self.betToMatch = 0
        self.pot = 0
        self.deck = dealer.getDeck()
        self.barrier = barrier.Barrier(numPlayers)

    def listen(self):
        self.sock.listen(5)
        while True:
            if len(self.players) < numPlayers:
                client, address = self.sock.accept()
                client.settimeout(300)
                myPlayer = Player(client, True)
                myThread = threading.Thread(target = self.listenToClient, args=(myPlayer, address))
                self.players.append(myPlayer)
                myThread.start()

    def broadcast(self, msg):
        for player in self.players:
            player.send(msg)

    def listenToClient(self, myPlayer, address):
        size = 1024
        name = ""
        myBet = 0
        while True:
            try:
                data = myPlayer.connection.recv(size)
                if data:
                    print data
                    if data == "NEWGAME":
                        if myPlayer.connection == self.players[0].connection:
                            self.deck = dealer.getDeck()
                        myPlayer.active = True
                        self.pot = 0
                        myPlayer.connection.send("READY")
                    elif data[0:8] == "REGISTER":
                        if len(self.players) > numPlayers:
                            myPlayer.connection.send("QUIT")
                            raise ValueError
                        else:
                            message = "REGISTERED"
                            if len(self.players) < numPlayers:
                                message += " W"
                            myPlayer.connection.send(message)
                            name = data.split()[1]
                            print name, "registered"
                            self.barrier.wait()
                    elif data == "STARTGAME":
                        if self.players[0] == myPlayer:
                            dealer.shuffleDeck(self.deck)
                            self.pot = 5 * numPlayers
                            self.currentPlayer = (self.currentPlayer + 1) % numPlayers
                        self.barrier.wait()
                        myPlayer.connection.send("START")
                    elif data == "GETSHAREDCARDS":
                        myPlayer.connection.send(json.dumps(self.deck[0:5]))
                    elif data == "GETHAND":
                        for i in range(len(self.players)):
                            if self.players[i] == myPlayer:
                                myPlayer.connection.send(json.dumps(self.deck[5+2*i:7+2*i]))
                    elif data == "GETOTHERHANDS":
                        others = []
                        for i in range(len(self.players)):
                            if self.players[i] != myPlayer:
                                others.append(self.deck[5+2*i:7+2*i])
                        myPlayer.connection.send(json.dumps(others))
                    elif data == "FIRSTBET":
                        while True:
                            if self.players[self.currentPlayer] == myPlayer:
                                if not myPlayer.active:
                                    myPlayer.connection.send("INACTIVE")
                                elif sum([1 for x in self.players if x.active]) == 1:
                                    myPlayer.connection.send("WINNER")
                                elif self.betToMatch == 0:
                                    myPlayer.connection.send("BETPASS")
                                else:
                                    myPlayer.connection.send("CALLRAISEFOLD " + str(self.betToMatch))
                                move = myPlayer.connection.recv(size)
                                if move[0] == 'b':
                                    self.pot += int(move.split()[1])
                                    myBet = int(move.split()[1])
                                    self.betToMatch = int(move.split()[1])
                                elif move[0] == 'r':
                                    self.pot += int(move.split()[1])
                                    myBet = int(move.split()[1])
                                    self.betToMatch = int(move.split()[1])
                                elif move[0] == 'c':
                                    myBet = self.betToMatch
                                    self.pot += self.betToMatch
                                elif move[0] == 'f':
                                    myPlayer.active = False
                                myPlayer.connection.send("PROCEED")
                                self.currentPlayer = (self.currentPlayer + 1) % numPlayers
                                self.barrier.wait()
                                break
                    elif data == "SECONDBET":
                        if myPlayer.active and myBet < self.betToMatch:
                            myPlayer.connection.send("CALLFOLD " + str(self.betToMatch) + " " + str(myBet))
                            move = myPlayer.connection.recv(size)
                            if move[0] == 'f':
                                myPlayer.active = False
                            elif move[0] == 'c':
                                self.pot += self.betToMatch - myBet
                        else:
                            myPlayer.connection.send("GARBAGE")
                            print "NO SECOND TURN"
                        self.barrier.wait()
                        self.betToMatch = 0
                        myBet = 0
                    elif data == "GETPOT":
                        myPlayer.connection.send(str(self.pot))
                else:
                    print "{0} disconnected".format(name)
                    myPlayer.connection.close()
                    self.players.remove(myPlayer)
                    return False
            except:
                myPlayer.connection.close()
                print "{0} disconnected".format(name)
                self.players.remove(myPlayer)
                return False

if __name__ == "__main__":
    ThreadedServer(ip, port).listen()
