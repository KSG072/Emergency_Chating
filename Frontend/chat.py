# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yugyeongjin/Desktop/chat.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

# 1. 채팅 내용을 DB 를 통해서 불러와 QListView 에다가 보여줘야함
# 2. 글을 입력하고 전송 버튼을 누르면 DB 에 올라가야댐
# 3. Login.py 와 연동을 시켜 로그인 정보를 chat.py 에 보내줘야댐
# 3.1 로그인을하고 로컬db에 저장된 로그인 정보를 불러옴
#


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 640)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 내용 적는곳
        self.Send = QtWidgets.QTextEdit(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(10, 476, 401, 110))
        self.Send.setObjectName("Send")
        # 전송버튼
        self.Send_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Send_Button.setGeometry(QtCore.QRect(410, 489, 71, 90))
        self.Send_Button.setObjectName("Send_Button")
        #보내지나 테스트
        self.Send_Button.clicked.connect(self.nd)

        # 채팅 리스트 (DB에서 정보를 불러와 보여줘야댐)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-5, 1, 491, 461))
        self.listView.setObjectName("listView")
        #test
        # box.addWidget(self.listView)

        MainWindow.setCentralWidget(self.centralwidget)
        # 잘모르겠습니다.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # self.Send_Button.clicked.connect(self.Send_DB)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Send_Button.setText(_translate("MainWindow", "전송"))

    #test
    def nd(self):
        # Msg = self.Send.text()
        self.Send.clear()
        # self.listView.addItem(QListWidgetItem(Msg))

    # def Send_DB:
    #     Msg = self.Send.text()
    #     #(NickName, Msg, Time)을 DB 로 이동
    #
    # def Bring_DB:
    #     #DB(NickName, Msg, Time)을 받아와 List_View에 보냄



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
