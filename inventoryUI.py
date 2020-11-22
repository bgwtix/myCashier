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
        self.inventoryBox = QGroupBox('清单')
        self.inventoryWidget = QTableWidget()
        self.inventorySearchButton = QPushButton('查询')
        self.firstPageButton = QPushButton('<<')
        self.previousPageButton = QPushButton('<')
        self.nextPageButton = QPushButton('>')
        self.lastPageButton = QPushButton('>>')
        self.pageEdit = QLineEdit()
        self.currentPage = 0
        self.totalPage = 0
        self.itemsPerPage = int(self.config["itemsPerPage"])
        self.pageLabel = QLabel('0/0')
        self.gotoEditPageButton = QPushButton('GO')

        self.addInventoryBoxLayout()
        self.showInventoryUILayout()

    def showInventoryUILayout(self):
        """
        显示货物清单界面
        """
        Layout = QGridLayout()
        Layout.addWidget(self.inventoryBox, 0, 0, 1, 1)
        Layout.setColumnStretch(0, 1)
        Layout.setRowStretch(0, 1)
        self.inventoryTab.setLayout(Layout)

    def addInventoryBoxLayout(self):
        """
        新增自定义界面
        """
        Layout = QGridLayout()
        titles = ['商品号', '详情', '单价', '库存', '累计进货量']
        self.inventoryWidget.setColumnCount(len(titles))
        self.inventoryWidget.setHorizontalHeaderLabels(titles)
        self.inventoryWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        self.inventoryWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择整行
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.pageEdit.setValidator(QRegExpValidator(regExp1, self))

        if 'itemsPerPage' not in self.config:
            self.config.setdefault('itemsPerPage', 20)
            self.saveConfigFunction()
        self.inventoryWidget.setRowCount(int(self.config["itemsPerPage"]))
        Layout.addWidget(self.inventoryWidget, 0, 0, 1, 0)
        Layout.addWidget(self.inventorySearchButton, 1, 0, 1, 1)
        Layout.addWidget(self.firstPageButton, 1, 1, 1, 1)
        Layout.addWidget(self.previousPageButton, 1, 2, 1, 1)
        Layout.addWidget(self.pageLabel, 1, 3, 1, 1)
        Layout.addWidget(self.nextPageButton, 1, 4, 1, 1)
        Layout.addWidget(self.lastPageButton, 1, 5, 1, 1)
        Layout.addWidget(self.pageEdit, 1, 6, 1, 1)
        Layout.addWidget(self.gotoEditPageButton, 1, 7, 1, 1)

        self.inventoryBox.setLayout(Layout)
