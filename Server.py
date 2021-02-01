import socketserver
import socket
import sys
from ChatSystem import ChatSystem
from Encryption import Encryption


class TCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip().decode('utf-8')

        res = data.find("ACK:")
        b = 0

        if(res != -1):
            b = int(data[res+4:])
            
        enc = Encryption()
        
        self.wfile.write(bytes("ACK:" + str(enc.getA()) + "\n", "utf-8"))
        
        print("hey")
        enc.makeFinalKey(b)

        if Connection.message != "":
            self.wfile.write(bytes(enc.encrypt(Connection.message)))
        else:
            msg = self.rfile.readline().strip().decode('utf-8')
            decrypted = enc.decrypt(msg)
            ChatSystem.messagesToDisplay.append(decrypted)



class Connection(object):
    message = ""

    def __init__(self, isHost):
        self.isHost = isHost

    def sendMessage(self):
        if self.isHost == "Y":
            self.runServer()
        else:
            self.runClient()

    def runServer(self):
        HOST = "localhost"
        PORT = 9999

        with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
            server.serve_forever()

    def runClient(self):
        HOST = "localhost"
        PORT = 9999
        
        enc = Encryption()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes("ACK:" + str(enc.getA()) + "\n", "utf-8"))

            data = str(sock.recv(1024), "utf-8")

            res = data.find("ACK:")
            b = 0

            if(res != -1):
                b = int(data[res+4:])
                    
            enc.makeFinalKey(b)

            if Connection.message != "":
                sock.sendall(bytes(enc.encrypt(Connection.message)))
            else:
                msg = str(sock.recv(1024), "utf-8")
                decrypted = enc.decrypt(msg)
                ChatSystem.messagesToDisplay.append(decrypted)
            

