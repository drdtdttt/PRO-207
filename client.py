import socket
from  threading import Thread
from tkinter import *
from tkinter import ttk

SERVER = None
PORT = 8080
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE=4096

name = None
listbox = None
textarea= None
labelchat = None
text_message = None

def connectToServer():
    global SERVER
    global name
    global sending_file

    cname = name.get()
    SERVER.send(cname.encode())

def openChatWindow():

    # -------Teacher Activity Start---
    print("\n\t\t\t\tIp MESSEGNGER")

    #Client GUI starts here
    window=Tk()

    window.title('Messenger')
    window.geometery("500x350")

    global name
    global listbox 
    global textarea
    global labelchat 
    global text_message
    global filePathLabel

    nameLabel = Label(window, text="Enter Your Name", font = ("Calibri", 10))
    nameLabel.place(x=10, y=8)

    name = Entry(window,width=30, font = ("Calibri", 10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window,text = "Connect to Chat Server", bd=1, font=("Calibri",10), command = connectToServer)
    connectserver.place(x=350,y=6)

    sepreator =ttk.Sepreator(window, orient='horizontal')
    sepretor.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text="Active Users", font = ("Calibri,10"))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font=("Calibri", 10))
    listbox.place(x=10, y=70)

    scrollbar1 = scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.configure(command = listbox.yview)
    
    connectButton=Button(window,text="Connect",bd=1, font = ("Calibri", 10))
    connectButton.place(x=282,y=160)
    
    disconnectButton=Button(window,text="Disconnect",bd=1,font = ("Calibri", 10))
    disconnectButton.place(x=350, y=160)

    refresh=Button(window,text="Refresh", bd=1, font =("Calibri", 10))
    refresh.place(x=435,y=160)

    labelchat = Label(window, text="Chat Window", font = ("Calibri", 10))
    labelchat.place(x=10, y=180)

    textarea = Text(window, width = 67,height = 6,font = ("Calibri",10))
    textarea.place(x=10,y=200)

    scrollbar2 = Scrollbar(textarea)
    scrollbar2.place(relheight = 1,relx = 1)
    scrollbar2.config(command = listbox.yview)

    attach=Button(window,text="Attach & Send",bd=1, font = ("Calibri",10))
    attach.place(x=10,y=305)

    text_message = Entry(window, width =43, font = ("Calibri",12))
    text_message.pack()
    text_message.place(x=98,y=306)

    send=Button(window,text="Send",bd=1, font = ("Calibri", 12))
    send.place(x=450,y=305)

    filePathLabel = Label(window, text="",fg= "blue", font = ("Calibri",8))
    filePathLabel.place(x=10, y=330)

    window.mainloop

    #----------- Boilerlate Code Start---------

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    #----------- Boilerlate Code Start---------
    
    # Teacher Activity 1
    openChatWindow()

setup()