# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import platform
if platform.system() == 'Windows':
    import database
else:
    from Backend import database


class Ui_MainWindow(QtWidgets.QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 아이디 라벨
        self.N_ID = QtWidgets.QLabel(self.centralwidget)
        self.N_ID.setGeometry(QtCore.QRect(59, 50, 20, 31))
        self.N_ID.setObjectName("N_ID")
        MainWindow.setCentralWidget(self.centralwidget)

        # 아이디 입력란
        self.ID = QtWidgets.QLineEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(84, 50, 220, 30))
        self.ID.setClearButtonEnabled(True)
        self.ID.setObjectName("ID")

        # 패스워드 라벨
        self.N_Password = QtWidgets.QLabel(self.centralwidget)
        self.N_Password.setGeometry(QtCore.QRect(14, 100, 70, 31))
        self.N_Password.setObjectName("N_Password")

        # 패스워드 입력란
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(84, 100, 220, 30))
        self.Password.setFrame(True)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setDragEnabled(True)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")

        # 닉네임 라벨
        self.N_Nickname = QtWidgets.QLabel(self.centralwidget)
        self.N_Nickname.setGeometry(QtCore.QRect(50, 150, 70, 31))
        self.N_Nickname.setObjectName("N_Nickname")

        # 닉네임 입력란
        self.Nickname = QtWidgets.QLineEdit(self.centralwidget)
        self.Nickname.setGeometry(QtCore.QRect(84, 150, 220, 30))
        self.Nickname.setFrame(True)
        self.Nickname.setDragEnabled(True)
        self.Nickname.setClearButtonEnabled(True)
        self.Nickname.setObjectName("Nickname")

        # 닉네임 설명란
        self.N_Notice = QtWidgets.QLabel(self.centralwidget)
        self.N_Notice.setGeometry(QtCore.QRect(66, 180, 250, 31))
        self.N_Notice.setObjectName("N_Notice")

        # 만들기 버튼
        self.LG_Button = QtWidgets.QPushButton(self.centralwidget)
        self.LG_Button.setGeometry(QtCore.QRect(130, 250, 110, 32))
        self.LG_Button.setAutoDefault(False)
        self.LG_Button.setDefault(True)
        self.LG_Button.setObjectName("LG_Button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.LG_Button.clicked.connect(self.SUMessageBox)

    def SUMessageBox(self):
        #  데이터 베이스로 회원가입 정보 옮기기

        msgbox = QtWidgets.QMessageBox(self)
        id, pw, nick = self.ID.text(), self.Password.text(), self.Nickname.text()

        if database.searchid(id):
            msgbox.information(self, '알림', '중복된 아이디 입니다.', QtWidgets.QMessageBox.Yes)
        elif database.searchnick(nick):
            msgbox.information(self, '알림', '중복된 닉네임 입니다.', QtWidgets.QMessageBox.Yes)
        else:
            msgbox.information(self, '알림', '회원가입이 완료 되었습니다.', QtWidgets.QMessageBox.Yes)
            database.resister(id, nick, pw)
            sys.exit()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.N_ID.setText(_translate("MainWindow", "ID :"))
        self.N_Password.setText(_translate("MainWindow", "Password :"))
        self.N_Nickname.setText(_translate("MainWindow", "별명 :"))
        self.N_Notice.setText(_translate("MainWindow", "* 공백으로 두시면 익명으로 자동 저장됩니다. *"))
        self.LG_Button.setText(_translate("MainWindow", "만들기"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
