# -*- coding: utf-8 -*-
import socketserver
import threading
import sqlite3
import os
from datetime import datetime

HOST = ''
PORT = 9009
lock = threading.Lock()


class UserManager:
	def __init__(self):
		self.users = {}

	def addUser(self, username, conn, addr):
		if username in self.users:
			conn.send('이미 등록된 사용자입니다.\n'.encode())
			return None


		lock.acquire()
		self.users[username] = (conn, addr)
		lock.release()

		self.sendMessageToAll('[%s]님이 입장했습니다.' %username)
		print('+++ 대화 참여자 수 [%d]' %len(self.users))

		return username

<<<<<<< HEAD
	def removeUser(self, username): 
		if username not in self.users:
			return

		lock.acquire()
		del self.users[username]
		lock.release()

		self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)
		print('--- 대화 참여자 수 [%d]' % len(self.users))


=======
	def removeUser(self, username):
		if username not in self.users:
			return

			lock.acquire()
			del self.users[username]
			lock.release()

			self.sendMessageToAll('[%s]님이 퇴장했습니다.' %username)
			print('--- 대화 참여자 수 [%d]' %len(self.users))
>>>>>>> master

	def messageHandler(self, username, msg):

		if msg[0] != '/':
			self.sendMessageToAll('[%s] %s' %(username, msg))
			return 

		if msg.strip() == '/quit':
			self.removeUser(username)
<<<<<<< HEAD

=======
>>>>>>> master
			return -1

	def sendMessageToAll(self, msg):
		for conn, addr in self.users.values():
			conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
	userman = UserManager()

	def handle(self):
		print('[%s] 연결됨' %self.client_address[0])


		try:
			username = self.registerUsername()
			msg = self.request.recv(1024)
			while msg:
				add_chat(username, msg.decode())
				print(username, " : ", msg.decode())
				print(datetime.now())
				if self.userman.messageHandler(username, msg.decode()) == -1:
					self.request.close()
<<<<<<< HEAD

=======
>>>>>>> master
					break
				msg = self.request.recv(1024)


		except Exception as e:
			print(e)
<<<<<<< HEAD

		print('[%s] 접속종료' %self.client_address[0])
		self.userman.removeUser(username)
=======
			print('[%s] 접속종료' %self.client_address[0])
			self.userman.removeUser(username)
>>>>>>> master

	def registerUsername(self):
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
	create_db()
	try:
		server = ChatingServer((HOST, PORT), MyTcpHandler)
		server.serve_forever()
	except KeyboardInterrupt:
		server.shutdown()
		server.server_close()

<<<<<<< HEAD

=======
def chating():
	MyTcpHandler.handle()
	while True:
		msg = input()
		if msg == '/quit':
			socketserver.send(msg.encode())
			break
		socketserver.send(msg.encode())
>>>>>>> master




def create_db():
<<<<<<< HEAD

=======
	# 이후 코드를 채우세요.
    # 이전 숙제를 참고하세요.
>>>>>>> master
    file_name = '../Data/chat_log.db'


    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    table_create_sql = """CREATE TABLE IF NOT EXISTS chat(
    id integer primary key autoincrement,
    userid VARCHAR(32) not null,
    message text not null,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""

    cur.execute(table_create_sql)


def add_chat(userid, message):
    conn = sqlite3.connect('../Data/chat_log.db')
    cur = conn.cursor()

    chat = "INSERT INTO chat(userid, message, ts) values (?, ?, CURRENT_TIMESTAMP)"
    cur.execute(chat, (userid, message))
    conn.commit()

<<<<<<< HEAD


def list_chat(ts = None):
=======
# 상황에 따라 함수를 부르는 코드를 채우세요.

def list_chat(ts = None): # 이후 코드를 채우세요.
>>>>>>> master

    log = []
    conn = sqlite3.connect('../Data/chat_log.db')
    cur = conn.cursor()

    if ts != None:
        sql = "select * from chat where chat.ts >= ?"
        cur.execute(sql, (ts,))
    else:
        sql = "select * from chat where 1"
        cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        log.append(row)

    return log



runServer()
<<<<<<< HEAD

=======
# chating()
>>>>>>> master
		
