import socket
import threading

ip = 'localhost'
port = 12345

class ThreadedServer(object):

    def __init__(self, host, port):
        print "Starting poker server..."
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.players = []

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(300)
            myThread = threading.Thread(target = self.listenToClient, args=(client, address))
            self.players.append((client))
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
                    if data[0:6] == ("NAMEIS"):
                        name = data.split()[1]
                        self.broadcast(name + " has joined")
                    elif len(self.players) != 2:
                        print "sending wait"
                        response = "WAITFORPLAYERS"
                    elif data == "READY":
                        print "sending ready"
                        response = "Let's play"
                    client.send(response)
                else:
                    print "{0} disconnected".format(name)
                    client.close()
                    self.players.pop()
                    return False
            except:
                client.close()
                print "{0} timed out".format(name)
                self.players.pop()
                return False

if __name__ == "__main__":
    ThreadedServer(ip, port).listen()
