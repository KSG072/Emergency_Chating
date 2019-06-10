# -*- coding: utf-8 -*-
import socketserver
import threading
import platform
if platform.system() == 'Windows':
    import database
else:
    from Backend import database

HOST = ''
PORT = 9009
lock = threading.Lock()


class UserManager:
   def __init__(self):
      self.users = {}

   def addUser(self, username, conn, addr):#이미 gui에서 구현한 기능.. 필요한가..?
      if username in self.users:
         conn.send('이미 등록된 사용자입니다.\n'.encode())
         return None

      lock.acquire()
      self.users[username] = (conn, addr)
      lock.release()

      self.sendMessageToAll('[%s]님이 입장했습니다.' %username)#이거는 어떻게 채팅방에 나오게 할까.. 관리자이름으로 db에 저장해서 출력할까
      print('+++ 대화 참여자 수 [%d]' %len(self.users))

      return username

   def removeUser(self, username):
      if username not in self.users:
         return

      lock.acquire()
      del self.users[username]
      lock.release()

      self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)#24번과 같은 방식으로 할 수 있으려나..
      print('--- 대화 참여자 수 [%d]' % len(self.users))


   def messageHandler(self, username, msg):#이제 나가기 버튼이 있는데 필요한 건가..

      if msg[0] != '/':
         self.sendMessageToAll('[%s] %s' %(username, msg))
         return

      if msg.strip() == '/quit':
         self.removeUser(username)
         return -1

   def sendMessageToAll(self, msg):
      for conn, addr in self.users.values():
         conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
   userman = UserManager()

   def handle(self):
      print('[%s] 연결됨' %self.client_address[0])

      try:
         username = ''#로그인할때 id의 닉네임을 불러와야함
         msg = self.request.recv(1024)
         while msg:
            database.add_chat(username, msg.decode())
            print(username, " : ", msg.decode())
            if self.userman.messageHandler(username, msg.decode()) == -1:
               self.request.close()

               break
            msg = self.request.recv(1024)
      except Exception as e:
          print(e)
          print('[%s] 접속종료' %self.client_address[0])
          self.userman.removeUser(username)



   def registerUsername(self):#이젠 필요 없지 않을까..
      while True:
         self.request.send('로그인ID:'.encode())
         username = self.request.recv(1024)
         username = username.decode().strip()

         if self.userman.addUser(username, self.request, self.client_address):
            return username


class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
   pass


def runServer():
   print('start')
   database.create_db()
   try:
      server = ChatingServer((HOST, PORT), MyTcpHandler)
      server.serve_forever()
   except KeyboardInterrupt:
      server.shutdown()
      server.server_close()

runServer()