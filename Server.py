import socketserver
import socket
import sys
from Encryption import Encryption


class TCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip().decode('utf-8')

        res = self.data.find("ACK:")
        b = 0

        if(res != -1):
            b = int(self.data[res+4:])
            
        enc = Encryption()
        
        self.wfile.write(bytes("ACK:" + str(enc.getA()) + "\n", "utf-8"))
        
        enc.makeFinalKey(b)

        if Connection.message != "":
            self.wfile.write(bytes(enc.encrypt(Connection.message)))
        else:
            msg = self.rfile.readline().strip().decode('utf-8')
            decrypted = enc.decrypt(msg)



class Connection(object):
    message = ""

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
            

