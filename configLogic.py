#!/usr/bin/python3
# -*- coding: utf-8 -*-
import scipy.io as scio
import sys
import os


def configLogicNotificationCenter(ui, msgType, msg=None):
    """

    :param ui:
    :param msgType:
    :param msg:
    """
    if msgType == "purchaseModeChanged":
        if msg:
            ui.purchaseMode.setText('进货模式开启')
            ui.config['purchaseMode'] = 1
            ui.insertTab(3, ui.purchaseTab, "进货系统")
        else:
            ui.purchaseMode.setText('进货模式关闭')
            ui.config['purchaseMode'] = 0
            ui.removeTab(3)
        ui.saveConfigFunction()

class configLogicInit:
    """
    会员界面逻辑
    """

    # 构造函数
    def __init__(self, ui):
        if int(ui.config['purchaseMode']):
            ui.purchaseMode.setCheckState(2)
        else:
            ui.removeTab(3)
        ui.purchaseMode.stateChanged.connect(
            lambda: configLogicNotificationCenter(ui, "purchaseModeChanged", ui.purchaseMode.checkState()))
