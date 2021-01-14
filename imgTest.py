from PIL import Image
from numpy import asarray

import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

pg.setConfigOptions(imageAxisOrder='row-major')

app = QtGui.QApplication([])
# load the image
image = Image.open('cinci.jpg')
# convert image to numpy array
data = asarray(image)

win = QtGui.QMainWindow()
win.resize(800,800)
imv = pg.ImageView()
win.setCentralWidget(imv)
win.show()
win.setWindowTitle('pyqtgraph example: ImageView')

imv.setImage(data)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()