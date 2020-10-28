#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class inventoryUIInit(QTabWidget):
    """
    货物清单界面
    """
    # 构造函数
    def __init__(self):
        super().__init__()
        self.inventoryTab = QWidget()


