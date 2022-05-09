import os
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets                     # uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, 
                             QLabel, QVBoxLayout)              # +++

from test2_ui import Ui_Form                                   # +++

class video (QtWidgets.QDialog, Ui_Form):
    def __init__(self,Form1):
        super().__init__()                  

#        uic.loadUi('test2.ui',self)                           # ---
        self.setupUi(Form1)                                     # +++

        self.control_bt.clicked.connect(self.start_webcam)
        # self.capture.clicked.connect(self.capture_image)
        # self.capture.clicked.connect(self.startUIWindow)       # - ()

        self.image_label.setScaledContents(True)

        self.cap = None                                        #  -capture <-> +cap

        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 0

    @QtCore.pyqtSlot()
    def start_webcam(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  800)
        self.timer.start()

    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, image = self.cap.read()
        # simage     = cv2.flip(image, 1)
        self.displayImage(image, True)

   

    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            self.image_label.setPixmap(QtGui.QPixmap.fromImage(outImage))

 

# if __name__=='__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = video()
#     window.setWindowTitle('Sign Detection')
#     window.show()
#     sys.exit(app.exec_())