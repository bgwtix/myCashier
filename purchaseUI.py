#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class purchaseUIInit(QTabWidget):
    """
    进货界面
    """
    # 构造函数
    def __init__(self):
        super().__init__()
        self.purchaseTab = QWidget()

        self.addPurchaseBox = QGroupBox('新增货物类型')
        self.addPurchaseIdEdit = QLineEdit()
        self.addPurchaseIdResult = QLabel('请输入货物编号')
        self.addPurchasePurchasePriceEdit = QLineEdit()
        self.addPurchasePriceEdit = QLineEdit()
        self.addPurchaseRemarksEdit = QLineEdit()
        self.purchaseAddButton = QPushButton('新增货物类型')

        self.deletePurchaseBox = QGroupBox('删除货物类型')
        self.deletePurchaseIdEdit = QLineEdit()
        self.deletePurchaseIdResult = QLabel('请输入货物编号')
        self.deletePurchasePurchasePriceEdit = QLineEdit()
        self.deletePurchasePriceEdit = QLineEdit()
        self.deletePurchaseRemarksEdit = QLineEdit()
        self.purchaseDeleteButton = QPushButton('删除货物类型')

        self.addAddPurchaseBoxLayout()
        self.addDeletePurchaseBoxLayout()
        self.showPurchaseUILayout()

    def showPurchaseUILayout(self):
        """
        显示进货界面
        """
        Layout = QGridLayout()
        Layout.addWidget(self.addPurchaseBox, 0, 0, 1, 1)
        Layout.addWidget(self.deletePurchaseBox, 1, 0, 1, 1)
        Layout.setColumnStretch(1, 1)
        Layout.setRowStretch(5, 1)
        self.purchaseTab.setLayout(Layout)

    def addDeletePurchaseBoxLayout(self):
        """
        新增货物界面
        """
        Layout = QFormLayout()
        Layout1 = QFormLayout()
        Layout.setLabelAlignment(Qt.AlignRight)
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.deletePurchaseIdEdit.setValidator(QRegExpValidator(regExp1, self))
        self.deletePurchaseIdResult.setEnabled(False)
        self.purchaseDeleteButton.setEnabled(False)
        Layout1.addRow(self.deletePurchaseIdEdit, self.deletePurchaseIdResult)
        Layout.addRow('货物编号：', Layout1)
        Layout.addRow('进价：', self.deletePurchasePurchasePriceEdit)
        Layout.addRow('售价：', self.deletePurchasePriceEdit)
        Layout.addRow('货物描述：', self.deletePurchaseRemarksEdit)
        Layout.addRow(self.purchaseDeleteButton)

        self.deletePurchaseBox.setLayout(Layout)

    def addAddPurchaseBoxLayout(self):
        """
        新增货物界面
        """
        Layout = QFormLayout()
        Layout1 = QFormLayout()
        Layout.setLabelAlignment(Qt.AlignRight)
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.addPurchaseIdEdit.setValidator(QRegExpValidator(regExp1, self))
        regExp1 = QRegExp('\d{1,8}.\d{0,2}')  # 设置会员号为最大11位数字
        self.addPurchasePurchasePriceEdit.setValidator(QRegExpValidator(regExp1, self))
        self.addPurchasePriceEdit.setValidator(QRegExpValidator(regExp1, self))
        self.addPurchaseIdResult.setEnabled(False)
        self.purchaseAddButton.setEnabled(False)
        Layout1.addRow(self.addPurchaseIdEdit, self.addPurchaseIdResult)
        Layout.addRow('货物编号：', Layout1)
        Layout.addRow('进价：', self.addPurchasePurchasePriceEdit)
        Layout.addRow('售价：', self.addPurchasePriceEdit)
        Layout.addRow('货物描述：', self.addPurchaseRemarksEdit)

        Layout.addRow(self.purchaseAddButton)

        self.addPurchaseBox.setLayout(Layout)





