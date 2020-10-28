#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class VIPUIInit(QTabWidget):
    """
    会员界面
    """

    # 构造函数
    def __init__(self):
        super().__init__()
        self.VIPTab = QWidget()

        self.addMemberBox = QGroupBox('注册会员')
        self.addMemberIdEdit = QLineEdit()
        self.addMemberIdResult = QLabel('请输入会员卡号')
        self.addMemberNameEdit = QLineEdit()
        self.addMemberRechargeEdit = QLineEdit()
        self.memberAddButton = QPushButton('注册会员')

        self.deleteMemberBox = QGroupBox('注销会员')
        self.deleteMemberIdEdit = QLineEdit()
        self.deleteMemberIdResult = QLabel('请输入会员卡号')
        self.deleteMemberNameEdit = QLineEdit()
        self.deleteMemberMoneyEdit = QLineEdit()
        self.deleteMemberIntegralEdit = QLineEdit()
        self.memberDeleteButton = QPushButton('注销会员')

        self.memberRechargeBox = QGroupBox('会员充值/查询')
        self.memberRechargeIdEdit = QLineEdit()
        self.memberRechargeResult = QLabel('请输入会员卡号')
        self.memberRechargeNameEdit = QLineEdit()
        self.memberRechargeIntegralEdit = QLineEdit()
        self.memberRechargeBalanceEdit = QLineEdit()
        self.memberRechargeMoneyEdit = QLineEdit()
        self.memberRechargeButton = QPushButton('充值')

        self.addAddMemberBoxLayout()
        self.addDeleteMemberBoxLayout()
        self.memberRechargeBoxLayout()
        self.showVIPUILayout()

    def showVIPUILayout(self):
        """
        显示会员界面
        """
        Layout = QGridLayout()
        Layout.addWidget(self.addMemberBox, 0, 0, 1, 1)
        Layout.addWidget(self.deleteMemberBox, 1, 0, 1, 1)
        Layout.addWidget(self.memberRechargeBox, 0, 1, 2, 1)
        Layout.setColumnStretch(1, 1)
        Layout.setRowStretch(5, 1)
        self.VIPTab.setLayout(Layout)

    def addAddMemberBoxLayout(self):
        """
        添加会员界面
        """
        Layout = QFormLayout()
        Layout1 = QFormLayout()
        Layout.setLabelAlignment(Qt.AlignRight)
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.addMemberIdEdit.setValidator(QRegExpValidator(regExp1, self))
        self.addMemberNameEdit.setMaxLength(10)
        self.addMemberRechargeEdit.setValidator(QRegExpValidator(regExp1, self))
        self.memberAddButton.setEnabled(False)
        Layout1.addRow(self.addMemberIdEdit, self.addMemberIdResult)
        Layout.addRow('会员卡号：', Layout1)
        Layout.addRow('姓名：', self.addMemberNameEdit)
        Layout.addRow('充值金额：', self.addMemberRechargeEdit)
        Layout.addRow(self.memberAddButton)
        self.addMemberBox.setLayout(Layout)

    def addDeleteMemberBoxLayout(self):
        """
        删除会员界面
        """
        Layout = QFormLayout()
        Layout1 = QFormLayout()
        Layout.setLabelAlignment(Qt.AlignRight)
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.deleteMemberIdEdit.setValidator(QRegExpValidator(regExp1, self))
        self.deleteMemberNameEdit.setEnabled(False)
        self.deleteMemberMoneyEdit.setEnabled(False)
        self.deleteMemberIntegralEdit.setEnabled(False)
        self.memberDeleteButton.setEnabled(False)
        Layout1.addRow(self.deleteMemberIdEdit, self.deleteMemberIdResult)
        Layout.addRow('会员卡号：', Layout1)
        Layout.addRow('姓名：', self.deleteMemberNameEdit)
        Layout.addRow('积分：', self.deleteMemberIntegralEdit)
        Layout.addRow('余额：', self.deleteMemberMoneyEdit)
        Layout.addRow(self.memberDeleteButton)
        self.deleteMemberBox.setLayout(Layout)

    def memberRechargeBoxLayout(self):
        """
        会员充值界面
        """
        Layout = QFormLayout()
        Layout1 = QFormLayout()
        Layout.setLabelAlignment(Qt.AlignRight)
        regExp1 = QRegExp('\d{1,11}')  # 设置会员号为最大11位数字
        self.memberRechargeIdEdit.setValidator(QRegExpValidator(regExp1, self))
        self.memberRechargeResult.setEnabled(False)
        self.memberRechargeNameEdit.setEnabled(False)
        self.memberRechargeBalanceEdit.setEnabled(False)
        self.memberRechargeIntegralEdit.setEnabled(False)
        self.memberRechargeButton.setEnabled(False)
        Layout1.addRow(self.memberRechargeIdEdit, self.memberRechargeResult)
        Layout.addRow('会员卡号：', Layout1)
        Layout.addRow('姓名：', self.memberRechargeNameEdit)
        Layout.addRow('积分：', self.memberRechargeIntegralEdit)
        Layout.addRow('余额：', self.memberRechargeBalanceEdit)
        Layout.addRow('充值金额：', self.memberRechargeMoneyEdit)
        Layout.addRow(self.memberRechargeButton)
        self.memberRechargeBox.setLayout(Layout)




