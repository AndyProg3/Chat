from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("ETE C")

window.geometry('500x450')

window.resizable(height = False, width = False)

txt = Text(window, borderwidth=4)
txt.pack()



btn = Button(window, text="Send", bg = "#A0DEF2", font = ('times', 12, 'bold'))
btn.pack(side=BOTTOM, fill=X)

txt = Entry(window, width=60, borderwidth=2)
txt.pack(side=BOTTOM, fill=X)

window.mainloop()

class ChatSystem(object):
    messagesToDisplay = []

    def getInput(self):
        return input("Chat: ")

    def displayMessage(self):
        print("Messages: ")
        if len(ChatSystem.messagesToDisplay) > 0:
            print(ChatSystem.messagesToDisplay.pop(0))
            self.displayMessage()