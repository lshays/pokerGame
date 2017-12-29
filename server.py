import socket
import threading
import dealer
import barrier
import json

ip = 'localhost'
port = 12345
numPlayers = 2

class ThreadedServer(object):

    def __init__(self, host, port):
        print "Starting poker server..."
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.players = []
        self.deck = dealer.getDeck()
        self.barrier = barrier.Barrier(numPlayers)

    def listen(self):
        self.sock.listen(5)
        while True:
            if len(self.players) < numPlayers:
                client, address = self.sock.accept()
                client.settimeout(300)
                myThread = threading.Thread(target = self.listenToClient, args=(client, address))
                self.players.append(client)
                myThread.start()

    def broadcast(self, msg):
        for player in self.players:
            player.send(msg)

    def listenToClient(self, client, address):
        size = 1024
        name = ""
        while True:
            try:
                data = client.recv(size)
                if data:
                    if data[0:8] == ("REGISTER"):
                        if len(self.players) > numPlayers:
                            client.send("QUIT")
                        else:
                            client.send("REGISTERED")
                        name = data.split()[1]
                        print name, "ready"
                    elif len(self.players) != numPlayers:
                        client.send("WAITFORPLAYERS")
                    elif data == "STARTGAME":
                        if self.players[0] == client:
                            dealer.shuffleDeck(self.deck)
                        self.barrier.wait()
                        client.send("START")
                    elif data == "GETSHAREDCARDS":
                        client.send(json.dumps(self.deck[0:5]))
                    elif data == "GETHAND":
                        for i in range(len(self.players)):
                            if self.players[i] == client:
                                client.send(json.dumps(self.deck[5+2*i:7+2*i]))
                    elif data == "GETOTHERHANDS":
                        others = []
                        for i in range(len(self.players)):
                            if self.players[i] != client:
                                others.append(self.deck[5+2*i:7+2*i])
                        client.send(json.dumps(others))
                    elif data == "NEWGAME":
                        pass
                else:
                    print "{0} disconnected".format(name)
                    client.close()
                    self.players.remove(client)
                    return False
            except:
                client.close()
                print "{0} disconnected".format(name)
                self.players.remove(client)
                return False

if __name__ == "__main__":
    ThreadedServer(ip, port).listen()
