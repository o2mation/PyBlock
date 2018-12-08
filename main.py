import sys, os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *

from gui import MainWindow

from log import logger

os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '9999'
                                                     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())