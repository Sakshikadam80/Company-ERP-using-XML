# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainWindow1



class Ui_MainWindow0(object):
    
     def ok(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()
        
     def setupUi(self, MainWindow0):
          MainWindow0.setObjectName("MainWindow0")
          MainWindow0.resize(596, 551)
          MainWindow0.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(55, 209, 232, 255), stop:1 rgba(255, 255, 255, 255));")
          self.centralwidget = QtWidgets.QWidget(MainWindow0)
          self.centralwidget.setObjectName("centralwidget")
          self.label = QtWidgets.QLabel(self.centralwidget)
          self.label.setGeometry(QtCore.QRect(110, 20, 391, 81))
          font = QtGui.QFont()
          font.setPointSize(22)
          font.setBold(True)
          font.setWeight(75)
          self.label.setFont(font)
          self.label.setObjectName("label")
          self.label_username = QtWidgets.QLabel(self.centralwidget)
          self.label_username.setGeometry(QtCore.QRect(110, 140, 151, 51))
          font = QtGui.QFont()
          font.setPointSize(10)
          font.setBold(True)
          font.setWeight(75)
          self.label_username.setFont(font)
          self.label_username.setObjectName("label_username")
          self.label_password = QtWidgets.QLabel(self.centralwidget)
          self.label_password.setGeometry(QtCore.QRect(110, 220, 151, 51))
          font = QtGui.QFont()
          font.setPointSize(10)
          font.setBold(True)
          font.setWeight(75)
          self.label_password.setFont(font)
          self.label_password.setObjectName("label_password")
          self.username_input = QtWidgets.QLineEdit(self.centralwidget)
          self.username_input.setGeometry(QtCore.QRect(360, 140, 151, 41))
          font = QtGui.QFont()
          font.setPointSize(10)
          font.setBold(True)
          font.setWeight(75)
          self.username_input.setFont(font)
          self.username_input.setObjectName("username_input")
          self.password_input = QtWidgets.QLineEdit(self.centralwidget)
          self.password_input.setGeometry(QtCore.QRect(360, 230, 161, 41))
          font = QtGui.QFont()
          font.setPointSize(10)
          font.setBold(True)
          font.setWeight(75)
          self.password_input.setFont(font)
          self.password_input.setObjectName("password_input")
          self.submit_button = QtWidgets.QPushButton(self.centralwidget)
          self.submit_button.setGeometry(QtCore.QRect(240, 300, 121, 51))
          font = QtGui.QFont()
          font.setPointSize(12)
          font.setBold(True)
          font.setWeight(75)
          self.submit_button.setFont(font)
          self.submit_button.setObjectName("submit_button")
        
          #push button working
          self.submit_button.clicked.connect(self.handle_login)
        
          self.label_status = QtWidgets.QLabel(self.centralwidget)
          self.label_status.setGeometry(QtCore.QRect(110, 400, 221, 31))
          font = QtGui.QFont()
          font.setPointSize(10)
          font.setBold(True)
          font.setWeight(75)
          self.label_status.setFont(font)
          self.label_status.setObjectName("label_status")
          MainWindow0.setCentralWidget(self.centralwidget)
          self.menubar = QtWidgets.QMenuBar(MainWindow0)
          self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 22))
          self.menubar.setObjectName("menubar")
          MainWindow0.setMenuBar(self.menubar)
          self.statusbar = QtWidgets.QStatusBar(MainWindow0)
          self.statusbar.setObjectName("statusbar")
          MainWindow0.setStatusBar(self.statusbar)

          self.retranslateUi(MainWindow0)
          QtCore.QMetaObject.connectSlotsByName(MainWindow0)

     def retranslateUi(self, MainWindow0):
          _translate = QtCore.QCoreApplication.translate
          MainWindow0.setWindowTitle(_translate("MainWindow0", "MainWindow"))
          self.label.setText(_translate("MainWindow0", " LOGIN FORM"))
          self.label_username.setText(_translate("MainWindow0", "USERNAME"))
          self.label_password.setText(_translate("MainWindow0", "PASSWORD"))
          self.submit_button.setText(_translate("MainWindow0", "SUBMIT"))
          self.label_status.setText(_translate("MainWindow0", "Status"))

     def handle_login(self): 
          username = self.username_input.text()
          password = self.password_input.text()

          if username == 'admin' and password == 'password':
              self.label_status.setText('Login successful!')
              self.submit_button.clicked.connect(self.ok)
              self.submit_button.clicked.connect(MainWindow0.close)
          else:
              self.label_status.setText('Invalid Username or Password!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow0 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow0()
    ui.setupUi(MainWindow0)
    MainWindow0.show()
    sys.exit(app.exec_())
