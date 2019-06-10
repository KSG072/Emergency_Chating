# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yugyeongjin/Desktop/chat11.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
#
# 1. DB 에서 정보를 불러와 아이디와 패스워드를 검사
# 1.1 아이디가 존재하지 않으면 ID가 틀렸다
# 1.2 아이디가 있으나 패스워드가 없으면 패스워드가 틀렸다.
# 2 로그인을 하고난 다음에 chat.py 로 이동
# 3 로그인 정보를 chat.py 로 이동
# 3.1 로그인을 하고 그 정보를 로컬db로 저장


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import os
import platform
if platform.system() == 'Windows':
    import database
else:
    from Backend import database





class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        #폼크기
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        #회원가입 버튼
        self.Sign_UP_Button = QtWidgets.QPushButton(Dialog)
        self.Sign_UP_Button.setGeometry(QtCore.QRect(129, 540, 110, 32))
        self.Sign_UP_Button.setObjectName("Sign_UP_Button")
        #id 라벨
        self.N_ID = QtWidgets.QLabel(Dialog)
        self.N_ID.setGeometry(QtCore.QRect(106, 450, 30, 31))
        self.N_ID.setObjectName("N_ID")
        #ip 라벨
        self.N_IP = QtWidgets.QLabel(Dialog)
        self.N_IP.setGeometry(QtCore.QRect(106, 400, 150, 31))
        self.N_IP.setObjectName("N_IP")
        #password 라벨
        self.N_Password = QtWidgets.QLabel(Dialog)
        self.N_Password.setGeometry(QtCore.QRect(54, 500, 80, 31))
        self.N_Password.setObjectName("N_Password")
        #id 입력
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setGeometry(QtCore.QRect(130, 450, 220, 30))
        self.ID.setClearButtonEnabled(True)
        self.ID.setObjectName("ID")
        #password 입략
        self.Password = QtWidgets.QLineEdit(Dialog)
        self.Password.setGeometry(QtCore.QRect(130, 500, 220, 30))
        self.Password.setFrame(True)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setDragEnabled(True)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        #로그인 버튼
        self.LG_Button = QtWidgets.QPushButton(Dialog)
        self.LG_Button.setGeometry(QtCore.QRect(240, 540, 110, 32))
        self.LG_Button.setObjectName("LG_Button")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #로그인 버튼 일어나면 생기는 일
        self.LG_Button.clicked.connect(self.LGMessageBox)
        self.Sign_UP_Button.clicked.connect(self.SUMessageBox)

    def SUMessageBox(self):
        msgbox = QtWidgets.QMessageBox(self)
        if platform.system() == 'Windows':
            subprocess.run(['sign_up.py'], shell = True)
        else:
            subprocess.Popen(['python3', 'sign_up.py'], cwd =os.path.dirname(os.path.realpath(__file__)))

    def LGMessageBox(self):
        msgbox = QtWidgets.QMessageBox(self)
        if database.searchid(self.ID.text()): #1234가 아닌 DB 안에 존재하는 ID 와 검사
            if database.searchpw(self.ID.text(),self.Password.text()): #1234가 아닌 DB 안에 존재하는 Password 와 검사
                msgbox.information(self, '알림', '로그인이 되었습니다.', QtWidgets.QMessageBox.Yes)

                Nick = database.nick(self.ID.text())
                if platform.system() == 'Windows':
                    subprocess.run(['chat.py'], shell=True)
                else:
                    subprocess.Popen(['python3', 'chat.py'], cwd=os.path.dirname(os.path.realpath(__file__)))

            else:
                msgbox.information(self, '알림', '비밀번호가 틀렸습니다.', QtWidgets.QMessageBox.Yes)
        else:
            msgbox.information(self, '알림', '없는 아이디 입니다.', QtWidgets.QMessageBox.Yes)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "로그인"))
        self.Sign_UP_Button.setText(_translate("Dialog", "회원가입"))
        self.N_IP.setText(_translate("Dialog", ipn))
        self.N_ID.setText(_translate("Dialog", "ID :"))
        self.N_Password.setText(_translate("Dialog", "Password : "))
        self.LG_Button.setText(_translate("Dialog", "로그인"))

if __name__ == "__main__":
    import sys
    database.create_user_db()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
