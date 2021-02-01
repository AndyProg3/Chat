from Server import Connection
from ChatSystem import ChatSystem
import threading
import time

def getInput(chat, con):
    Connection.message = chat.getInput()
    con.sendMessage()
    
def display(chat):
    count = 0
    while count <= 15:
        time.sleep(10)
        chat.displayMessage()
        count += 1

host = input("Would you like to host? (Y/N): ")

chat = ChatSystem()
con = Connection(host)

try:
   threading.Thread(target = display, args=(chat,))
except:
   print ("Error: unable to start thread")

count = 0
while count <= 15:
    getInput(chat, con)
    count += 1
