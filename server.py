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
            self.players.append(myThread)
            myThread.start()

    def listenToClient(self, client, address):
        print "Player {0} joined".format(len(self.players))
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    if len(self.players) != 2:
                        response = "Waiting on {0} more player(s) to join".format(2-len(self.players))
                    elif data == "STARTGAME":
                        response = "Let's play"
                    client.send(response)
                else:
                    print "Player {0} disconnected".format(len(self.players))
                    client.close()
                    self.players.pop()
                    return False
            except:
                client.close()
                print "Player {0} timed out".format(len(self.players))
                self.players.pop()
                return False

if __name__ == "__main__":
    ThreadedServer(ip, port).listen()
