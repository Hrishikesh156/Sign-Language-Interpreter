# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res

class register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
        Form.resize(941, 739)
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
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(460, 10, 461, 711))
        self.label_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.fname = QtWidgets.QLineEdit(self.widget)
        self.fname.setGeometry(QtCore.QRect(540, 190, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fname.setFont(font)
        self.fname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QLineEdit(self.widget)
        self.lname.setGeometry(QtCore.QRect(540, 260, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lname.setFont(font)
        self.lname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lname.setObjectName("lname")
        self.registerBTN = QtWidgets.QPushButton(self.widget)
        self.registerBTN.setGeometry(QtCore.QRect(530, 580, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.registerBTN.setFont(font)
        self.registerBTN.setStyleSheet("QPushButton#registerBTN\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#registerBTN:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#registerBTN:pressed{\n"
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
        self.registerBTN.setObjectName("registerBTN")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(530, 650, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,210)")
        self.label_4.setObjectName("label_4")
        self.LoginPage = QtWidgets.QPushButton(self.widget)
        self.LoginPage.setGeometry(QtCore.QRect(660, 650, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LoginPage.setFont(font)
        self.LoginPage.setStyleSheet("border:none;\n"
"color:rgb(8, 127, 255);\n"
"")
        self.LoginPage.setObjectName("LoginPage")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(540, 50, 261, 71))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(540, 330, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.email.setObjectName("email")
        self.pswd = QtWidgets.QLineEdit(self.widget)
        self.pswd.setGeometry(QtCore.QRect(540, 410, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pswd.setFont(font)
        self.pswd.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.pswd.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.pswd.setObjectName("pswd")
        self.confirm_pswd = QtWidgets.QLineEdit(self.widget)
        self.confirm_pswd.setGeometry(QtCore.QRect(540, 490, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_pswd.setFont(font)
        self.confirm_pswd.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.confirm_pswd.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.confirm_pswd.setObjectName("confirm_pswd")
        self.pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Register Page"))
        Form.setWindowIcon(QtGui.QIcon('logo.png'))
        self.fname.setPlaceholderText(_translate("Form", "First Name"))
        self.lname.setPlaceholderText(_translate("Form", "Last Name"))
        self.registerBTN.setText(_translate("Form", "Register"))
        self.label_4.setText(_translate("Form", "Already a user?"))
        self.LoginPage.setText(_translate("Form", "Login here."))
        self.label_5.setText(_translate("Form", "REGISTER"))
        self.email.setPlaceholderText(_translate("Form", "Email ID"))
        self.pswd.setPlaceholderText(_translate("Form", "Password"))
        self.confirm_pswd.setPlaceholderText(_translate("Form", "Confirm Password"))
