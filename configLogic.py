#!/usr/bin/python3
# -*- coding: utf-8 -*-
import scipy.io as scio
import sys
import os


def configLogicNotificationCenter(ui, msgType, msg=None):
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

    # dataFile = 'G://Cashier//config.mat'
    # dict = {'key': 2, 'data': 100}
    # scio.savemat(dataFile, dict)

    # 构造函数
    def __init__(self, ui):
        print(ui.config['purchaseMode'][0])
        if ui.config['purchaseMode'][0]:
            ui.purchaseMode.setCheckState(2)
            print(1)
        else:
            ui.removeTab(3)
            print(0)
        ui.purchaseMode.stateChanged.connect(
            lambda: configLogicNotificationCenter(ui, "purchaseModeChanged", ui.purchaseMode.checkState()))
