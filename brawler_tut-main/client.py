import socket

class Client():
    def __init__(self):
        self.PORT = 55000
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = '!DISCONNECT'
        self.SERVER = "192.168.56.1"
        #self.SERVER = "26.198.250.47"
        self.ADDR = (self.SERVER, self.PORT)
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect(self.ADDR)
        self.clientsocket.settimeout(0.002)
        self.connected = True

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        self.clientsocket.send(message)



