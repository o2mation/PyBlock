#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qframer import views, collectView


class BaseToolButton(QPushButton):
    """docstring for BaseButton"""

    def __init__(self, text, parent=None):
        super(BaseToolButton, self).__init__()
        self.parent = parent
        self.setFlat(True)
        self.setCheckable(True)
        self.setFixedSize(60, 60)
        self.setText(text)


class NavgationBar(QFrame):

    viewID = "NavgationBar"

    @collectView
    def __init__(self, buttonIds, parent=None):
        super(NavgationBar, self).__init__(parent)
        self.parent = parent
        self.setObjectName("NavgationBar")
        self.buttonIds = buttonIds
        self.initData()
        self.initUI()

    def initData(self):
        self.buttons = {}

    def initUI(self):
        baseWidth = 60
        self.setFixedWidth(baseWidth)
        mainLayout = QVBoxLayout()
        for buttonId in self.buttonIds:
            setattr(self, "%sButton" % buttonId, BaseToolButton(buttonId))
            button = getattr(self, "%sButton" % buttonId)
            button.setObjectName(buttonId)
            mainLayout.addWidget(button)
            self.buttons.update({buttonId: button})

        mainLayout.addStretch()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        for buttonId, button in self.buttons.items():
            button.clicked.connect(self.checkedButton)

    def checkedButton(self):
        self.sender().setChecked(True)
        for buttonId, button in self.buttons.items():
            if button is not self.sender():
                button.setChecked(False)
