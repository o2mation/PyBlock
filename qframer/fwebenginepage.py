#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *

class FWebEngineView(QWebEngineView):

    def __init__(self, parent=None):
        super(FWebEngineView, self).__init__(parent)
        self.parent = parent
    

