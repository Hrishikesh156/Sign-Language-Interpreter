import os
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets                     
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, 
                             QLabel, QVBoxLayout)
# from SignDetect import detect_fn              

from test2_ui import Ui_Form   

import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

import os
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

import cv2 
import numpy as np

import time
import pyttsx3
# global prev_val,start_time,language,engine
engine = pyttsx3.init()
language = 'en'
prev_val = None
start_time = None
seconds = 3

WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'
CUSTOM_MODEL_NAME = 'my_ssd_mobnet' 
CONFIG_PATH = MODEL_PATH+'/'+CUSTOM_MODEL_NAME+'/pipeline.config'


@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-21')).expect_partial()

category_index = label_map_util.create_category_index_from_labelmap(ANNOTATION_PATH+'/label_map.pbtxt')


class video (QtWidgets.QDialog, Ui_Form):
    global prev_val,start_time,language,engine
    engine = pyttsx3.init()
    language = 'en'
    prev_val = None
    start_time = None
    def __init__(self):
        super().__init__()                  

#        uic.loadUi('test2.ui',self)                           # ---
        self.setupUi(self)                                     # +++

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
            # self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            # self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
            # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  700)
        self.timer.start()

     
    # @tf.function
    # def detect_fn(image):
    #     image, shapes = detection_model.preprocess(image)
    #     prediction_dict = detection_model.predict(image, shapes)
    #     detections = detection_model.postprocess(prediction_dict, shapes)
    #     return detections

    @QtCore.pyqtSlot()
    def update_frame(self):
        global prev_val,start_time,language,engine,seconds
        ret, frame = self.cap.read()
        image_np = np.array(frame)
    
        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        detections = detect_fn(input_tensor)
        
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                    for key, value in detections.items()}
        detections['num_detections'] = num_detections

        # detection_classes should be ints.
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

        label_id_offset = 1
        image_np_with_detections = image_np.copy()

        viz_utils.visualize_boxes_and_labels_on_image_array(
                    image_np_with_detections,
                    detections['detection_boxes'],
                    detections['detection_classes']+label_id_offset,
                    detections['detection_scores'],
                    category_index,
                    use_normalized_coordinates=True,
                    max_boxes_to_draw=5,
                    min_score_thresh=.5,
                    agnostic_mode=False)
           
        classes = detections['detection_classes']+label_id_offset
        score = detections['detection_scores']
        class_name = category_index[classes[0]]['name']
        
        if(score[0] > 0.8):
            new_val = class_name
            current_time = time.time()
            if(start_time != None):
                elapsed_time = current_time - start_time
                if(elapsed_time>seconds):
                    prev_val = None

            if(new_val != prev_val):
                start_time = time.time()
                seconds = 3
                print(new_val)
                engine.say(new_val)
                # engine.runAndWait()
                prev_val = new_val   
            else:
                # print("same value")
                pass
      
            
        image = cv2.resize(image_np_with_detections, (800, 600))
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

    def startUIWindow(self):
        self.Window = UIWindow()                               # - self
        self.setWindowTitle("UIWindow")

#        self.setCentralWidget(self.Window)
#        self.show()
### +++ vvv
        self.Window.ToolsBTN.clicked.connect(self.goWindow1)

        self.hide()
        self.Window.show()

    def goWindow1(self):
        self.show()
        self.Window.hide()
### +++ ^^^


class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)

        self.resize(300, 300)
        self.label = QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.ToolsBTN = QPushButton('text')
#        self.ToolsBTN.move(50, 350)

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.label)
        self.v_box.addWidget(self.ToolsBTN)
        self.setLayout(self.v_box)


# if __name__=='__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = video()
#     window.setWindowTitle('main code')
#     window.show()
#     sys.exit(app.exec_())