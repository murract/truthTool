import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import PyQt5.QtWidgets as qtw
import cv2

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QHBoxLayout())  
        self.resize(1500,800)
        self.controlPad()
        self.displayPad()
        self.show()


    def controlPad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QVBoxLayout())

        #Buttons
        
        btn_import = qtw.QPushButton('Import Truthing', clicked = lambda: self.func_result())
        btn_save = qtw.QPushButton('Save Truthing', clicked = lambda: self.clear_calc()) 
        btn_genChips = qtw.QPushButton('Gen Chips',clicked = lambda: self.num_press('9'))
        btn_autoSave = qtw.QPushButton('Auto Save',clicked = lambda: self.num_press('8'))
        btn_draw = qtw.QPushButton('Draw Truth',clicked = lambda: self.num_press('7'))
        btn_edit = qtw.QPushButton('Edit Truth',clicked = lambda: self.num_press('6'))
        btn_Bedit = qtw.QPushButton('Batch Edit Truth',clicked = lambda: self.num_press('5'))
        btn_clear = qtw.QPushButton('Clear Truth',clicked = lambda: self.num_press('4'))
        btn_copy = qtw.QPushButton('Copy',clicked = lambda: self.num_press('3'))
        btn_paste = qtw.QPushButton('Paste',clicked = lambda: self.num_press('2'))
        btn_interpolate = qtw.QPushButton('Interpolate',clicked = lambda: self.num_press('1'))
        btn_tmatcher = qtw.QPushButton('Start Template Matcher',clicked = lambda: self.num_press('0'))
        btn_help = qtw.QPushButton('Help',clicked = lambda: self.func_press('+'))
        btn_sliderOptions = qtw.QPushButton('Slider Options',clicked = lambda: self.func_press('-'))
        btn_lock = qtw.QPushButton('Lock Zoom',clicked = lambda: self.func_press('*'))
        btn_info = qtw.QPushButton('info',clicked = lambda: self.func_press('/'))

        #add buttons to layout
        fileIO = qtw.QWidget()
        fileIO.setLayout(qtw.QVBoxLayout())
        fileIO.layout().addWidget(qtw.QLabel('File I/O'))
        fileIO.layout().addWidget(btn_import)
        fileIO.layout().addWidget(btn_save)
        fileIO.layout().addWidget(btn_genChips)
        fileIO.layout().addWidget(btn_autoSave)
        container.layout().addWidget(fileIO)

        container.layout().addWidget(btn_draw)
        container.layout().addWidget(btn_edit)
        container.layout().addWidget(btn_Bedit)
        container.layout().addWidget(btn_clear)
        container.layout().addWidget(btn_copy)
        container.layout().addWidget(btn_paste)

        container.layout().addWidget(btn_interpolate)
        container.layout().addWidget(btn_tmatcher)

        container.layout().addWidget(btn_help)
        container.layout().addWidget(btn_sliderOptions)
        container.layout().addWidget(btn_lock)
        container.layout().addWidget(btn_info)
        self.layout().addWidget(container,2)

    def displayPad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QVBoxLayout())

        #add title
        title = qtw.QLabel('File Name')             ####ADD STUFF TO MAKE THIS SHOW FILE NAME
        title.setAlignment(QtCore.Qt.AlignCenter)
        container.layout().addWidget(title,1)

        #add image viewer
        pg.setConfigOptions(imageAxisOrder='row-major')
        imv = pg.ImageView()
        container.layout().addWidget(imv,10)
        self.layout().addWidget(container,8)

        
        cap = cv2.VideoCapture('bunny.mp4')
        frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

        fc = 1
        ret = True

        while (fc < frameCount  and ret):
            ret, buf[fc] = cap.read()
            fc += 1

        cap.release()

        cv2.waitKey(0)
        
        imv.setImage(buf)
        imv.play(rate = 30)
        
        #add video control panel and controls
        controlPanel = qtw.QWidget()
        controlPanel.setLayout(qtw.QHBoxLayout())
        play_btn = qtw.QPushButton('Play')
        next_btn = qtw.QPushButton('Next Frame')
        prev_btn = qtw.QPushButton('Previous Frame')
        controlPanel.layout().addWidget(prev_btn,1)
        controlPanel.layout().addWidget(play_btn,1)
        controlPanel.layout().addWidget(next_btn,1)
        container.layout().addWidget(controlPanel)


        




app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
