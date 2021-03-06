# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res

class login(object):
    switch_window = QtCore.pyqtSignal()    
    def setupUi(self, Form):
            
        Form.setObjectName("Form")
        Form.resize(941, 739)
        Form.setFixedSize(941,739)
        Form.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 931, 730))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 441, 711))
        self.label.setStyleSheet("border-image: url(:/images/background.jpg);\n"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(460, 10, 461, 711))
        self.label_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.userid = QtWidgets.QLineEdit(self.widget)
        self.userid.setGeometry(QtCore.QRect(540, 190, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userid.setFont(font)
        self.userid.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.userid.setObjectName("userid")
        self.pswd = QtWidgets.QLineEdit(self.widget)
        self.pswd.setGeometry(QtCore.QRect(540, 290, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pswd.setFont(font)
        self.pswd.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.pswd.setObjectName("pswd")
        self.loginBTN = QtWidgets.QPushButton(self.widget)
        self.loginBTN.setGeometry(QtCore.QRect(540, 400, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.loginBTN.setFont(font)
        self.pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginBTN.setStyleSheet("QPushButton#loginBTN{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#loginBTN:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#loginBTN:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}")
        self.loginBTN.setObjectName("loginBTN")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(550, 470, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,210)")
        self.label_4.setObjectName("label_4")
        self.RegisterPage = QtWidgets.QPushButton(self.widget)
        self.RegisterPage.setGeometry(QtCore.QRect(640, 470, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RegisterPage.setFont(font)
        self.RegisterPage.setStyleSheet("border:none")
        self.RegisterPage.setObjectName("RegisterPage")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(540, 50, 231, 71))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


      
        # self.RegisterPage.clicked.connect(self.show_register)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('logo.png'))
        # set the title
        # self.setWindowTitle("Icon")
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.userid.setPlaceholderText(_translate("Form", "User ID"))
        self.pswd.setPlaceholderText(_translate("Form", "password"))
        self.loginBTN.setText(_translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "New user?"))
        self.RegisterPage.setText(_translate("Form", "Register"))
        self.label_5.setText(_translate("Form", "LOGIN"))

#     def show_register(self):
#             print("clicked")    
      
# if __name__ == "__main__":
#         app = QtWidgets.QApplication(sys.argv)
        # Form = QtWidgets.QWidget()
        # ui = login()
        # ui.setupUi(Form)
        # Form.show()
#         sys.exit(app.exec_())