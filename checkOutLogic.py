#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import sys
import time
import scipy.io as scio
import numpy as np
import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

G_shoppingCartWidget = None
G_totalPrice = None


def checkOutLogicNotificationCenter(ui, msgType, msg=None):
    """
    结账界面通知中心
    :param ui:
    :param msgType: 消息类型：
                                    "QueryMemberInformationByVIPID"：根据会员卡号查询会员信息
                                    "QueryProductInformationByVIPID"：根据商品号查询商品信息
                                    "addCurrentItemToShoppingCart"：将当前货物添加到购物车
    :param msg: 输入信息，可以为空
    """
    if msgType == "QueryMemberInformationByVIPID":  # 根据会员号查询会员信息
        if len(msg) < 11:
            ui.VIPId.setText('')
            ui.VIPName.setText("卡号长度不足")
            ui.VIPIntegral.setText('')
            ui.VIPMoney.setText('')
            return
        sql = "SELECT * FROM vip WHERE vipID = %s"
        ui.myCursor.execute(sql % msg)
        myResult = ui.myCursor.fetchone()  # 查询单条
        if myResult is None:
            ui.VIPId.setText('')
            ui.VIPName.setText("未查询到会员信息: %s" % msg)
            ui.VIPIntegral.setText('')
            ui.VIPMoney.setText('')
        else:
            ui.VIPId.setText(msg)
            ui.VIPName.setText(myResult['name'])
            ui.VIPIntegral.setText(str(myResult['integral']))
            ui.VIPMoney.setText(str(myResult['money']))

    elif msgType == "QueryProductInformationByGoodsID":  # 根据货物序号查询货物信息
        sql = "SELECT * FROM cashier WHERE goodsID = %s"
        ui.myCursor.execute(sql % msg)
        myResult = ui.myCursor.fetchone()  # 查询单条
        if myResult is None:
            ui.checkOutPrice.setText('')
            ui.checkOutIDSelected.setText('')
            ui.checkOutRemarks.setText('无效的商品号：%s' % msg)
            ui.checkOutStock.setText('')
        else:
            ui.checkOutPrice.setText('%.2f' % myResult['price'])
            ui.checkOutIDSelected.setText(msg)
            ui.checkOutRemarks.setText(str(myResult['remarks']))
            ui.checkOutStock.setText(str(myResult['stock']))

    elif msgType == "addCurrentItemToShoppingCart":  # 将当前货物添加到购物车
        if ui.checkOutPrice.text() != '':
            rowCnt = ui.shoppingCartWidget.rowCount()
            currentItemID = []
            for row in range(rowCnt):
                goodsID = int(ui.shoppingCartWidget.item(row, 0).text())
                goodsNum = int(ui.shoppingCartWidget.item(row, 3).text())
                if currentItemID.count(goodsID) == 0:
                    currentItemID.append(goodsID)
                if currentItemID.count(int(ui.checkOutIDSelected.text())):
                    goodsNum += 1
                    ui.shoppingCartWidget.setItem(row, 3, QTableWidgetItem(str(goodsNum)))
                    goodsPrice = float(ui.shoppingCartWidget.item(row, 2).text())
                    totalPrice = '%.2f' % (goodsNum * goodsPrice)
                    ui.shoppingCartWidget.setItem(row, 4, QTableWidgetItem(totalPrice))
                    break
            else:
                ui.shoppingCartWidget.setRowCount(rowCnt + 1)
                ui.shoppingCartWidget.setItem(rowCnt, 0,
                                              QTableWidgetItem(ui.checkOutIDSelected.text()))
                ui.shoppingCartWidget.setItem(rowCnt, 1,
                                              QTableWidgetItem(ui.checkOutRemarks.text()))
                ui.shoppingCartWidget.setItem(rowCnt, 2,
                                              QTableWidgetItem(ui.checkOutPrice.text()))
                ui.shoppingCartWidget.setItem(rowCnt, 3,
                                              QTableWidgetItem("1"))
                goodsPrice = float(ui.shoppingCartWidget.item(rowCnt, 2).text())
                totalPrice = '%.2f' % goodsPrice
                ui.shoppingCartWidget.setItem(rowCnt, 4, QTableWidgetItem(totalPrice))
            rowCnt = ui.shoppingCartWidget.rowCount()
            totalPrice = 0
            for row in range(rowCnt):
                totalPrice += float(ui.shoppingCartWidget.item(row, 4).text())
            ui.totalPrice.setText('%.2f' % totalPrice)
    elif msgType == "paymentB":
        if float(ui.totalPrice.text()) > 0:

            if ui.VIPId.text() != '' and float(ui.VIPMoney.text()) > float(ui.totalPrice.text()):
                vipFlag = 1
                message = '确认结账？'
            else:
                vipFlag = 0
                message = '会员卡余额不足, 确认结账？'
            reply = QMessageBox.question(ui, '信息', message,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                if vipFlag:
                    sql = "UPDATE vip SET money=%s, integral=%s WHERE vipID = %s LIMIT 1"
                    money = float(ui.VIPMoney.text()) - float(ui.totalPrice.text())
                    integral = float(ui.VIPIntegral.text()) + float(ui.totalPrice.text())
                    val = (str(money), str(integral), ui.VIPId.text())
                    myResult = ui.myCursor.execute(sql % val)
                    if myResult == 1:
                        ui.memberRechargeBalanceEdit.setText(str(money))
                        ui.memberRechargeMoneyEdit.setText('')
                        ui.myDb.commit()
                        ui.VIPIntegral.setText(str(integral))
                        ui.VIPMoney.setText(str(money))
                        ui.totalPrice.setText('0.00')

                        nowTime = time.time()
                        row_num = ui.shoppingCartWidget.rowCount()

                        filePath = os.path.dirname(os.path.realpath(sys.argv[0])) + '//log//' + \
                                   str(datetime.datetime.now().year) + '_' + str(datetime.datetime.now().month) + \
                                   '//VIP'
                        if os.path.exists(filePath) is False:
                            try:
                                os.makedirs(filePath)
                            except Exception as e:
                                print(e)
                        fileName = filePath + '//%s.mat' % ui.VIPId.text()
                        if os.path.isfile(fileName) is not False:
                            vipLog = scio.loadmat(fileName, squeeze_me=True)
                            vipLog.pop('__header__')
                            vipLog.pop('__version__')
                            vipLog.pop('__globals__')
                        else:
                            vipLog = {'timeStamp': [],
                                      'goodsID': [],
                                      'goodCount': [],
                                      'goodPrice': [],
                                      }
                        for row in range(row_num):
                            vipLog['timeStamp'] = np.append(vipLog['timeStamp'], nowTime)

                            vipLog['goodsID'] = np.append(vipLog['goodsID'],
                                                          int(ui.shoppingCartWidget.item(0, 0).text()))
                            vipLog['goodPrice'] = np.append(vipLog['goodPrice'],
                                                            float(ui.shoppingCartWidget.item(0, 2).text()))
                            vipLog['goodCount'] = np.append(vipLog['goodCount'],
                                                            int(ui.shoppingCartWidget.item(0, 3).text()))
                            ui.shoppingCartWidget.removeRow(0)
                        QMessageBox.about(ui, '成功', '交易成功')
                        scio.savemat(fileName, vipLog)


def checkOutLogicCustomContextMenu(pos):
    """
    设置自定义菜单
    :param ui:
    :param pos:
    """
    global G_shoppingCartWidget, G_totalPrice
    row_num = []
    col_num = []
    try:
        for i in G_shoppingCartWidget.selectionModel().selection().indexes():
            if i.row() not in row_num:  # 获取选中的行
                row_num.append(i.row())
            if i.column() not in col_num:  # 获取选中的列
                col_num.append(i.column())
    except Exception as e:
        print(e)
    menu = QMenu()
    addOneAction = menu.addAction('+1')
    addFiveAction = menu.addAction('+5')
    addTenAction = menu.addAction('+10')
    subtractOneAction = menu.addAction('-1')
    subtractFiveAction = menu.addAction('-5')
    subtractTenAction = menu.addAction('-10')
    clearTenAction = menu.addAction('删除')
    action = menu.exec_(G_shoppingCartWidget.mapToGlobal(pos))
    if action == addOneAction:
        for row in row_num:
            goodsNum = int(G_shoppingCartWidget.item(row, 3).text())
            goodsNum += 1
            G_shoppingCartWidget.setItem(row, 3, QTableWidgetItem(str(goodsNum)))
            goodsPrice = float(G_shoppingCartWidget.item(row, 2).text())
            totalPrice = '%.2f' % (goodsNum * goodsPrice)
            G_shoppingCartWidget.setItem(row, 4, QTableWidgetItem(totalPrice))
    elif action == addFiveAction:
        for row in row_num:
            goodsNum = int(G_shoppingCartWidget.item(row, 3).text())
            goodsNum += 5
            G_shoppingCartWidget.setItem(row, 3, QTableWidgetItem(str(goodsNum)))
            goodsPrice = float(G_shoppingCartWidget.item(row, 2).text())
            totalPrice = '%.2f' % (goodsNum * goodsPrice)
            G_shoppingCartWidget.setItem(row, 4, QTableWidgetItem(totalPrice))
    elif action == addTenAction:
        for row in row_num:
            goodsNum = int(G_shoppingCartWidget.item(row, 3).text())
            goodsNum += 10
            G_shoppingCartWidget.setItem(row, 3, QTableWidgetItem(str(goodsNum)))
            goodsPrice = float(G_shoppingCartWidget.item(row, 2).text())
            totalPrice = '%.2f' % (goodsNum * goodsPrice)
            G_shoppingCartWidget.setItem(row, 4, QTableWidgetItem(totalPrice))
    elif action == subtractOneAction:
        rowRemoved = 0
        for row in row_num:
            goodsNum = int(G_shoppingCartWidget.item(row - rowRemoved, 3).text())
            if goodsNum > 1:
                goodsNum -= 1
                G_shoppingCartWidget.setItem(row - rowRemoved, 3, QTableWidgetItem(str(goodsNum)))
                goodsPrice = float(G_shoppingCartWidget.item(row, 2).text())
                totalPrice = '%.2f' % (goodsNum * goodsPrice)
                G_shoppingCartWidget.setItem(row - rowRemoved, 4, QTableWidgetItem(totalPrice))
            else:
                G_shoppingCartWidget.removeRow(row - rowRemoved)
                rowRemoved += 1
    elif action == subtractFiveAction:
        rowRemoved = 0
        for row in row_num:
            goodsNum = int(G_shoppingCartWidget.item(row - rowRemoved, 3).text())
            if goodsNum > 5:
                goodsNum -= 5
                G_shoppingCartWidget.setItem(row - rowRemoved, 3, QTableWidgetItem(str(goodsNum)))
                goodsPrice = float(G_shoppingCartWidget.item(row, 2).text())
                totalPrice = '%.2f' % (goodsNum * goodsPrice)
                G_shoppingCartWidget.setItem(row - rowRemoved, 4, QTableWidgetItem(totalPrice))
            else:
                G_shoppingCartWidget.removeRow(row - rowRemoved)
                rowRemoved += 1
    elif action == subtractTenAction:
        rowRemoved = 0
        for row in row_num:
            goodsNum = int(G_shoppingCartWidget.item(row - rowRemoved, 3).text())
            if goodsNum > 10:
                goodsNum -= 10
                G_shoppingCartWidget.setItem(row - rowRemoved, 3, QTableWidgetItem(str(goodsNum)))
                goodsPrice = float(G_shoppingCartWidget.item(row, 2).text())
                totalPrice = '%.2f' % (goodsNum * goodsPrice)
                G_shoppingCartWidget.setItem(row - rowRemoved, 4, QTableWidgetItem(totalPrice))
            else:
                G_shoppingCartWidget.removeRow(row - rowRemoved)
                rowRemoved += 1
    elif action == clearTenAction:
        rowRemoved = 0
        for row in row_num:
            G_shoppingCartWidget.removeRow(row - rowRemoved)
            rowRemoved += 1
    rowCnt = G_shoppingCartWidget.rowCount()
    totalPrice = 0
    for row in range(rowCnt):
        totalPrice += float(G_shoppingCartWidget.item(row, 4).text())
    G_totalPrice.setText('%.2f' % totalPrice)


class checkOutLogicInit:
    """
    结账界面逻辑
    """

    # 构造函数
    def __init__(self, ui):
        global G_shoppingCartWidget, G_totalPrice
        G_shoppingCartWidget = ui.shoppingCartWidget
        G_totalPrice = ui.totalPrice
        # 添加购物车右键选择功能-暂时不可用
        G_shoppingCartWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        G_shoppingCartWidget.customContextMenuRequested.connect(checkOutLogicCustomContextMenu)

        ui.VIPIdText.editingFinished.connect(
            lambda: checkOutLogicNotificationCenter(ui, "QueryMemberInformationByVIPID",
                                                    ui.VIPIdText.text()))
        ui.checkOutInputIDText.editingFinished.connect(
            lambda: checkOutLogicNotificationCenter(ui, "QueryProductInformationByGoodsID",
                                                    ui.checkOutInputIDText.text()))
        ui.addToShoppingCartButton.clicked.connect(
            lambda: checkOutLogicNotificationCenter(ui, "addCurrentItemToShoppingCart"))
        ui.paymentButton.clicked.connect(
            lambda: checkOutLogicNotificationCenter(ui, "paymentB"))
