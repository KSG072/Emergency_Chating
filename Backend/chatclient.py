import socket
from threading import Thread

host = ''
PORT = 9009

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())#이게 받는건데 여기서 클라이언트의 DB에 저장가능하지 않을까...

        except:
            pass

def check(HOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.settimeout(1)
        try: sock.connect((HOST, PORT))
        except Exception as e:
            return False
        return True



def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            if msg == '/quit':
                sock.send(msg.encode())#보내면서 DB에 저장을 할까..
                break
            sock.send(msg.encode())