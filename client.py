import socket

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 12345
SIZE = 1024

class Client(object):

    def __init__(self, host, port):
        print "Connecting to server..."
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print "Connection successful"

    def send(self, message):
        self.socket.send(message)

    def receive(self):
        return self.socket.recv(SIZE)

if __name__ == "__main__":
    myClient = Client(SERVER_IP, PORT_NUMBER)
    while True:
        data = raw_input("ECHO THIS: ")
        myClient.send(data)
        response = myClient.receive()
        if not response:
            print "Connection terminated"
            myClient.socket.close()
            break
        print response
