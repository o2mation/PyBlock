#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qframer import collectView
from qframer import FWebEngineView

from log import logger

class WebViewPage(FWebEngineView):

    viewID = "WebViewPage"

    @collectView
    def __init__(self, parent=None):
        super(WebViewPage, self).__init__(parent)
        self.setObjectName("WebViewPage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        logger.info("%s", os.getcwd())
        index_path = os.path.join(os.getcwd(), "web", "index.html")
        logger.info("%s", index_path)
        url = QUrl().fromLocalFile(index_path)
        self.load(url)
