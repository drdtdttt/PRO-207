import socket
from threading import Thread

SERVER = None
PORT = 8000
IP_ADDRESS = '127.0.0.1'


clients = {}
userNames=[]

def acceptConnections():
    global clients
    global SERVER

    while True:
        client.addr = SERVER.accept()
        print(client,addr)

def setup():
    print("\n")
    print("\t\t\t\t\t\t*** LUDO LADDER ***")


    global SERVER
    global PORT
    global IP_ADDRESS

   
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")


    acceptConnections()
setup_thread = Thread(target=setup)
setup_thread.start()


setup()
    
    
