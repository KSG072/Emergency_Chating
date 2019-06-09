# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat1.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import socket
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

host = ''

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())

        except:
            pass

def check(HOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.settimeout(1)
        try: sock.connect((HOST, 9009))
        except Exception as e:
            return False
        return True



def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, 9009))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            if msg == '/quit':
                sock.send(msg.encode())
                break
            sock.send(msg.encode())


class Ui_MainWindow(QtWidgets.QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #채팅 내용
        self.chating = QtWidgets.QTextBrowser(self.centralwidget)
        self.chating.setGeometry(QtCore.QRect(-1, -1, 481, 501))
        self.chating.setObjectName("chating")
        #입력 받는곳
        self.send = QtWidgets.QTextEdit(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(7, 506, 400, 101))
        self.send.setObjectName("send")
        #전송 버튼
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(407, 517, 71, 91))
        self.send_button.setObjectName("send_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.send_button.clicked.connect(self.send_text)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emergency Chating"))
        self.send_button.setText(_translate("MainWindow", "전송"))

    def send_text(self):
        text = self.send.toPlainText() #입력받은 텍스트
        self.chating.append("NickName" + " : " + text)   #DB에서 추출해서 할까..
        self.send.clear()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    runChat()
    sys.exit(app.exec_())
