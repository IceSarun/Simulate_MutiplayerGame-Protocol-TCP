from socket import*
import pickle


class Network:
    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.server = "192.168.1.11"
        self.port = 12500
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getPose(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except error as e:
            print(e)      