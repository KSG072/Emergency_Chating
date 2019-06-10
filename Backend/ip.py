# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import socket

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import os
import platform



import Backend.login

def check(HOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.settimeout(3)
        try: sock.connect((HOST, 9009))
        except Exception as e:
            print(e)
            return False
        return True

class Ui_MainWindow(QtWidgets.QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(213, 130)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #확인버튼
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(54, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 80, 16))
        self.label.setObjectName("label")
        #ip 입력창
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 213, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.ipp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "확인"))
        self.label.setText(_translate("MainWindow", "Sever IP : "))

    #확인 클릭시 ip, port 검사
    def ipp(self):
        msgbox = QtWidgets.QMessageBox(self)
        ip = self.lineEdit.text()
        self.lineEdit.clear()
        if not check(ip):
            msgbox.information(self, "알림", "맞지 않는 주소입니다.", QtWidgets.QMessageBox.Yes)
        else:
<<<<<<< refs/remotes/origin/master
=======
            Backend.login.host = ip
>>>>>>> 조금수정
            msgbox.information(self, "알림", "접속 성공", QtWidgets.QMessageBox.Yes)

            if platform.system() == 'Windows':
                subprocess.run(['login.py'], shell = True)
            else:
                subprocess.Popen(['python3', 'login.py'], cwd =os.path.dirname(os.path.realpath(__file__)))








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
