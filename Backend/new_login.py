# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from threading import Thread
import subprocess
import os
import platform
import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            text = data.decode()
            ui.receive_text(text)

        except:
            pass

def seder(sock, text1):
    sock.send(text1.encode())

class Ui_MainWindow(QtWidgets.QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background:rgb(254,240,27)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.N_img = QLabel(MainWindow)
        self.N_img.setPixmap(QPixmap("rion.PNG"))
        self.N_img.setGeometry(90,30,300,300)

        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(240, 500, 113, 32))
        self.Login_Button.setObjectName("Login_Button")
        #회원가입 버튼입니다.
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 500, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(180, 410, 170, 21))
        self.id.setClearButtonEnabled(True)
        self.id.setStyleSheet("background:rgb(255,255,255)")
        self.id.setObjectName("id")

        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(180, 450, 171, 21))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setClearButtonEnabled(True)
        self.password.setStyleSheet("background:rgb(255,255,255)")
        self.password.setObjectName("password")

        self.ip = QtWidgets.QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(180, 370, 170, 21))
        self.ip.setStyleSheet("background:rgb(255,255,255)")
        self.ip.setObjectName("ip")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(106, 452, 71, 16))
        self.password_label.setObjectName("password_label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(152, 413, 28, 16))
        self.label_2.setObjectName("label_2")

        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setGeometry(QtCore.QRect(152, 373, 28, 16))
        self.ip_label.setObjectName("ip_label")

        self.ip_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ip_Button.setGeometry(QtCore.QRect(365, 365, 71, 31))
        self.ip_Button.setObjectName("ip_Button")

        #채팅공간
        self.chating = QtWidgets.QTextBrowser(self.centralwidget)
        self.chating.setGeometry(QtCore.QRect(-1, -1, 481, 501))
        self.chating.setStyleSheet("background:rgb(255,255,255)")
        self.chating.setEnabled(False)
        self.chating.setVisible(False)
        self.chating.setObjectName("chating")
        #채팅입력란
        self.send = QtWidgets.QTextEdit(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(7, 506, 400, 101))
        self.send.setStyleSheet("background:rgb(255,255,255)")
        self.send.setEnabled(False)
        self.send.setVisible(False)
        self.send.setObjectName("send")
        #전송버튼
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(407, 517, 71, 91))
        self.send_button.setStyleSheet("background:rgb(200,200,200)")
        self.send_button.setEnabled(False)
        self.send_button.setVisible(False)
        self.send_button.setObjectName("send_button")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)
        #회원가입 버튼, 로그인 버튼 누르먄
        self.Login_Button.clicked.connect(self.LGMessageBox)
        self.pushButton_2.clicked.connect(self.SUMessageBox)

        #ip접속 버튼 누르면
        self.ip_Button.clicked.connect(self.IPMessageBox)

        #채팅전송버튼 누르면
        self.send_button.clicked.connect(self.send_text)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def viewchange(self):
        self.Login_Button.setVisible(False)
        self.N_img.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.id.setVisible(False)
        self.password.setVisible(False)
        self.ip.setVisible(False)
        self.password_label.setVisible(False)
        self.label_2.setVisible(False)
        self.ip_label.setVisible(False)
        self.ip_Button.setVisible(False)
        self.id.setEnabled(False)
        self.password.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.Login_Button.setEnabled(False)
        self.chating.setVisible(True)
        self.send.setVisible(True)
        self.send_button.setVisible(True)
        self.chating.setEnabled(True)
        self.send.setEnabled(True)
        self.send_button.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EMERGENCY"))
        self.Login_Button.setText(_translate("MainWindow", "로그인"))
        self.pushButton_2.setText(_translate("MainWindow", "회원가입"))
        self.password_label.setText(_translate("MainWindow", "Password : "))
        self.label_2.setText(_translate("MainWindow", "ID : "))
        self.ip_label.setText(_translate("MainWindow", "IP :"))
        self.ip_Button.setText(_translate("MainWindow", "접속"))
        self.send_button.setText(_translate("MainWindow", "전송"))

    def IPMessageBox(self):
        msgbox = QtWidgets.QMessageBox(self)
        try:
            sock.settimeout(1)
            sock.connect((self.ip.text(), 9009))
            msgbox.information(self, "알림", "올바른 IP주소 입니다.")
            self.ip.setEnabled(False)
            self.ip_Button.setEnabled(False)
        except Exception as e:
            msgbox.information(self, "알림", "틀린 IP주소 입니다.", QtWidgets.QMessageBox.Yes)
            if platform.system() == 'Windows':
                subprocess.run(['new_login.py'], shell=True)
            else:
                subprocess.Popen(['python3', 'new_login.py'], cwd=os.path.dirname(os.path.realpath(__file__)))
            sys.exit()


    def SUMessageBox(self):
        msgbox = QtWidgets.QMessageBox(self)
        sock.send("sign".encode())
        time.sleep(0.5)
        sock.send(self.id.text().encode())
        time.sleep(0.5)
        sock.send(self.password.text().encode())
        result = sock.recv(1024).decode()
        print(result)
        if result == "issigned":
            msgbox.information(self, '알림', '중복된 ID입니다.', QtWidgets.QMessageBox.Yes)
        else:
            msgbox.information(self, '알림', '가입이 완료되었습니다. 로그인버튼을 눌러주세요.', QtWidgets.QMessageBox.Yes)

    def LGMessageBox(self):
        msgbox = QtWidgets.QMessageBox(self)
        sock.send("login".encode())
        time.sleep(0.5)
        sock.send(self.id.text().encode())
        time.sleep(0.5)
        sock.send(self.password.text().encode())
        result = sock.recv(1024).decode()
        print(result)
        if result == '로그인성공':
            msgbox.information(self, '알림', '로그인 되었습니다.', QtWidgets.QMessageBox.Yes)
            self.viewchange()
            time.sleep(0.5)
            t = Thread(target=rcvMsg, args=(sock,))
            t.daemon = True
            t.start()
        else:
            msgbox.information(self, '알림', '로그인에 실패했습니다.', QtWidgets.QMessageBox.Yes)

    def send_text(self):
        text = self.send.toPlainText()  # 입력받은 텍스트
        seder(sock, text)
        self.send.clear()

    def receive_text(self, text):
        self.chating.append(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

