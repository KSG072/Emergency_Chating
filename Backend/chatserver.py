# -*- coding: utf-8 -*-
import socketserver
import threading
import Backend.database

HOST = ''
PORT = 9009
lock = threading.Lock()


class UserManager:
   def __init__(self):
      self.users = {}

   def addUser(self, username, conn, addr):#이미 gui에서 구현한 기능.. 필요한가..?

      lock.acquire()
      self.users[username] = (conn, addr)
      lock.release()

      # self.sendMessageToAll('[%s]님이 입장했습니다.' %username)#이거는 어떻게 채팅방에 나오게 할까.. 관리자이름으로 db에 저장해서 출력할까
      # self.sendMessageToAll('+++ 대화 참여자 수 [%d]' %len(self.users))
      print('+++ 대화 참여자 수 [%d]' %len(self.users))

      return username

   def removeUser(self, username):
      if username not in self.users:
         return

      lock.acquire()
      del self.users[username]
      lock.release()

      self.sendMessageToAll('[%s]님이 퇴장했습니다.' %username)#24번과 같은 방식으로 할 수 있으려나..
      print('--- 대화 참여자 수 [%d]' %len(self.users))


   def messageHandler(self, username, msg):#이제 나가기 버튼이 있는데 필요한 건가..

      if msg[0] != '/':
         self.sendMessageToAll('[%s] : %s' %(username, msg))
         return

      if msg.strip() == '/quit':
         self.removeUser(username)
         return -1

   def sendMessageToAll(self, msg):
      for conn, addr in self.users.values():
         conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
   userman = UserManager()

   def login(self):
       id = self.request.recv(1024).decode()
       pw = self.request.recv(1024).decode()
       if Backend.database.searchid(id):
           if Backend.database.searchpw(id, pw):
               self.request.send('로그인성공'.encode())
               return True, self.userman.addUser(id, self.request, self.client_address)
           else:
               self.request.send('로그인실패'.encode())
               return False, ''
       else:
           self.request.send('로그인실패'.encode())
           return False, ''

   def signup(self):
       id = self.request.recv(1024).decode()
       pw = self.request.recv(1024).decode()
       if Backend.database.searchid(id):
           self.request.send("issigned".encode())
       else:
           Backend.database.resister(id, pw)
           self.request.send("signed".encode())

   def handle(self):
       print('[%s] 연결됨' %self.client_address[0])
       logined = False
       command = self.request.recv(1024).decode()
       print(command)
       while not logined:
           if command == "login":
                logined, username = self.login()
           else:
               self.signup()
           msg = self.request.recv(1024)
           command = msg.decode()
       try:
           while msg:
               Backend.database.add_chat(username, msg.decode())
               print(username, " : ", msg.decode())
               if self.userman.messageHandler(username, msg.decode()) == -1:
                   self.request.close()
                   break
               msg = self.request.recv(1024)
       except Exception as e:
           print(e)
           print('[%s] 접속종료' % self.client_address[0])
           self.userman.removeUser(username)



# self.userman.addUser(username, self.request, self.client_address):



class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
   pass


def runServer():
   print('start')
   Backend.database.create_db()
   try:
      server = ChatingServer((HOST, PORT), MyTcpHandler)
      server.serve_forever()
      server.server_bind()
   except KeyboardInterrupt:
      server.shutdown()
      server.server_close()

runServer()