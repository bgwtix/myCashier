#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class configUIInit(QTabWidget):
    """
    进货界面
    """
    # 构造函数
    def __init__(self):
        super().__init__()
        self.configTab = QWidget()
        self.customConfigBox = QGroupBox('新增货物类型')
        self.purchaseMode = QCheckBox("进货模式关闭")

        self.addCustomConfigBoxLayout()
        self.showConfigUILayout()

    def showConfigUILayout(self):
        """
        显示配置界面
        """
        Layout = QGridLayout()
        Layout.addWidget(self.customConfigBox, 0, 0, 1, 1)
        Layout.setColumnStretch(1, 1)
        Layout.setRowStretch(5, 1)
        self.configTab.setLayout(Layout)

    def addCustomConfigBoxLayout(self):
        """
        新增自定义界面
        """
        Layout = QFormLayout()
        Layout1 = QFormLayout()
        Layout.addRow(self.purchaseMode)
        self.customConfigBox.setLayout(Layout)



