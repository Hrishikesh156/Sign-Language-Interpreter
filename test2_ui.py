from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(931, 730)
        Form.setFixedSize(941,739)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)

        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)
        self.control_bt.resize(100,32)
        self.control_bt.setGeometry(200, 150, 100, 40)
        self.control_bt.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));color:rgba(255, 255, 255, 210);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "padding-left:5px;padding-top:5px;background-color:rgba(150, 123, 111, 255);"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));"
                             "}")

        self.back = QtWidgets.QPushButton(Form)
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.back.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));color:rgba(255, 255, 255, 210);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "padding-left:5px;padding-top:5px;background-color:rgba(150, 123, 111, 255);"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));"
                             "}")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
     

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form",     "Sign Detection"))
        self.control_bt.setText(_translate("Form", "Start"))
        self.back.setText(_translate("Form",    "back"))
        Form.setWindowIcon(QtGui.QIcon('logo.png'))