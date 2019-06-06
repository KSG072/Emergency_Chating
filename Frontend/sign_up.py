# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.N_Password = QtWidgets.QLabel(self.centralwidget)
        self.N_Password.setGeometry(QtCore.QRect(64, 500, 70, 31))
        self.N_Password.setObjectName("N_Password")
        self.ID = QtWidgets.QLineEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(134, 450, 220, 30))
        self.ID.setClearButtonEnabled(True)
        self.ID.setObjectName("ID")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(134, 500, 220, 30))
        self.Password.setFrame(True)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setDragEnabled(True)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        # 만들기 버튼
        self.LG_Button = QtWidgets.QPushButton(self.centralwidget)
        self.LG_Button.setGeometry(QtCore.QRect(180, 540, 110, 32))
        self.LG_Button.setAutoDefault(False)
        self.LG_Button.setDefault(True)
        self.LG_Button.setObjectName("LG_Button")
        self.N_ID = QtWidgets.QLabel(self.centralwidget)
        self.N_ID.setGeometry(QtCore.QRect(110, 450, 20, 31))
        self.N_ID.setObjectName("N_ID")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.LG_Button.clicked.connect(self.SUMessageBox)

    def SUMessageBox(self):
        #  데이터 베이스로 회원가입 정보 옮기기
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.N_Password.setText(_translate("MainWindow", "Password : "))
        self.LG_Button.setText(_translate("MainWindow", "만들기"))
        self.N_ID.setText(_translate("MainWindow", "ID :"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
