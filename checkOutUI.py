#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class checkOutUIInit(QTabWidget):
    """
    结账界面
    """
    # 构造函数
    def __init__(self):
        super().__init__()
        self.checkOutTab = QWidget()

        self.VIPBox = QGroupBox('会员信息')
        self.VIPIdText = QLineEdit()
        self.VIPId = QLineEdit()
        self.VIPName = QLineEdit()
        self.VIPIntegral = QLineEdit()
        self.VIPMoney = QLineEdit()

        self.checkOutInputBox = QGroupBox('商品信息查询')
        self.checkOutInputIDText = QLineEdit()
        self.checkOutIPInputCountText = QLineEdit()
        self.checkOutPrice = QLineEdit()
        self.checkOutRemarks = QLineEdit()
        self.checkOutStock = QLineEdit()
        self.addToShoppingCartButton = QPushButton('加入购物车')
        self.checkOutIDSelected = QLineEdit()

        self.checkOutShoppingCartBox = QGroupBox('购物车')
        self.shoppingCartWidget = QTableWidget()

        self.checkPaymentBoxBox = QGroupBox('账单汇总')
        self.totalPrice = QLabel('0.00')
        self.paymentButton = QPushButton('结账')

        self.addVIPBoxLayout()
        self.addCheckOutInputBoxLayout()
        self.addCheckOutShoppingCartBoxLayout()
        self.addPaymentBoxLayout()

        self.showLayout()

    def showLayout(self):
        """
        1
        """
        Layout = QGridLayout()
        Layout.addWidget(self.VIPBox, 0, 0, 1, 1)
        Layout.addWidget(self.checkOutInputBox, 1, 0, 1, 1)
        Layout.addWidget(self.checkPaymentBoxBox, 2, 0, 1, 1)
        Layout.addWidget(self.checkOutShoppingCartBox, 0, 1, 6, 1)
        Layout.setColumnStretch(1, 1)
        Layout.setRowStretch(5, 1)
        self.checkOutTab.setLayout(Layout)

    def addPaymentBoxLayout(self):
        """
        1
        """
        Layout = QFormLayout()
        Layout.addRow('总价', self.totalPrice)
        Layout.addRow(self.paymentButton)
        self.checkPaymentBoxBox.setLayout(Layout)

    def addCheckOutShoppingCartBoxLayout(self):
        """
        添加购物车界面
        """
        Layout = QGridLayout()
        titles = ['商品号', '详情', '单价', '数量', '价格']
        self.shoppingCartWidget.setColumnCount(len(titles))
        self.shoppingCartWidget.setHorizontalHeaderLabels(titles)
        self.shoppingCartWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        self.shoppingCartWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择整行
        Layout.addWidget(self.shoppingCartWidget, 0, 0, 1, 1)

        self.checkOutShoppingCartBox.setLayout(Layout)

    def addCheckOutInputBoxLayout(self):
        """
        添加商品信息查询界面
        """
        Layout = QFormLayout()
        Layout.setLabelAlignment(Qt.AlignRight)
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.checkOutInputIDText.setValidator(QRegExpValidator(regExp1, self))
        self.checkOutIDSelected.setReadOnly(True)
        self.checkOutPrice.setReadOnly(True)
        self.checkOutRemarks.setReadOnly(True)
        Layout1 = QFormLayout()
        Layout1.addRow(self.checkOutInputIDText, self.addToShoppingCartButton)

        Layout.addRow("商品号查询：", Layout1)
        Layout.addRow("商品号：", self.checkOutIDSelected)
        Layout.addRow("单价：", self.checkOutPrice)
        Layout.addRow('库存', self.checkOutStock)
        Layout.addRow("商品描述：", self.checkOutRemarks)
        self.checkOutInputBox.setLayout(Layout)

    def addVIPBoxLayout(self):
        """
        添加会员信息界面
        """
        Layout = QFormLayout()
        Layout.setLabelAlignment(Qt.AlignRight)
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.VIPIdText.setValidator(QRegExpValidator(regExp1, self))
        self.VIPId.setReadOnly(True)
        self.VIPName.setReadOnly(True)
        self.VIPIntegral.setReadOnly(True)
        self.VIPMoney.setReadOnly(True)
        Layout.addRow("会员卡号查询：", self.VIPIdText)
        Layout.addRow("会员卡号：", self.VIPId)
        Layout.addRow("姓名：", self.VIPName)
        Layout.addRow("积分：", self.VIPIntegral)
        Layout.addRow("余额：", self.VIPMoney)

        self.VIPBox.setLayout(Layout)
