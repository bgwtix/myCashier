#!/usr/bin/python3
# -*- coding: utf-8 -*-


def purchaseLogicNotificationCenter(ui, msgType, msg=None):
    """

    :param ui:
    :param msgType:
    :param msg:
    """
    if msgType == "addQueryPurchaseInformationByVIPID":  # 新增货物时根据会员号查询会员信息
        sql = "SELECT * FROM cashier WHERE goodsID = %s"
        ui.myCursor.execute(sql % msg)
        myResult = ui.myCursor.fetchone()  # 查询单条
        if myResult is None:
            ui.addPurchaseIdResult.setText(msg)
            ui.addPurchasePurchasePriceEdit.setText('')
            ui.addPurchaseRemarksEdit.setText('')
            ui.addPurchasePriceEdit.setText('')
            ui.purchaseAddButton.setEnabled(True)
        else:
            ui.addPurchaseIdResult.setText('货物编号已经存在%s' % msg)
            ui.addPurchaseRemarksEdit.setText(myResult['remarks'])
            ui.addPurchasePurchasePriceEdit.setText('%.2f' % myResult['purchasePrice'])
            ui.addPurchasePriceEdit.setText('%.2f' % myResult['price'])
            ui.purchaseAddButton.setEnabled(False)
    elif msgType == "addPurchaseInformation":
        if not (ui.addPurchaseRemarksEdit.text() == '' or
                ui.addPurchasePurchasePriceEdit.text() == '' or
                ui.addPurchasePriceEdit.text() == ''):
            sql = """INSERT INTO cashier(goodsID, price, Discount, purchasePrice, stock, accumulativeTotal, remarks)
                   VALUES (%s, %s, 1.00, %s, 0, 0, "%s")"""
            val = (ui.addPurchaseIdResult.text(), ui.addPurchasePriceEdit.text(),
                   ui.addPurchasePurchasePriceEdit.text(), ui.addPurchaseRemarksEdit.text())
            try:
                ui.myCursor.execute(sql % val)
                ui.myDb.commit()
                ui.addPurchaseIdResult.setText('新增货物成功')
                ui.purchaseAddButton.setEnabled(False)
            except Exception as e:
                ui.addPurchaseIdResult.setText(e)

    elif msgType == "deleteQueryPurchaseInformationByVIPID":  # 新增货物时根据会员号查询会员信息
        sql = "SELECT * FROM cashier WHERE goodsID = %s"
        ui.myCursor.execute(sql % msg)
        myResult = ui.myCursor.fetchone()  # 查询单条
        if myResult is None:
            ui.deletePurchaseIdResult.setText('货物编号不存在%s' % msg)
            ui.deletePurchasePurchasePriceEdit.setText('')
            ui.deletePurchaseRemarksEdit.setText('')
            ui.deletePurchasePriceEdit.setText('')
            ui.purchaseDeleteButton.setEnabled(False)
        else:
            ui.deletePurchaseIdResult.setText(msg)
            ui.deletePurchaseRemarksEdit.setText(myResult['remarks'])
            ui.deletePurchasePurchasePriceEdit.setText('%.2f' % myResult['purchasePrice'])
            ui.deletePurchasePriceEdit.setText('%.2f' % myResult['price'])
            ui.purchaseDeleteButton.setEnabled(True)
    elif msgType == "deletePurchaseInformation":  # 新增货物时根据会员号查询会员信息
        sql = """DELETE FROM cashier WHERE goodsID LIKE '%s' LIMIT 1"""
        val = (ui.deletePurchaseIdResult.text())
        try:
            length = ui.myCursor.execute(sql % val)
            if length:
                ui.myDb.commit()
                ui.purchaseAddButton.setEnabled(False)
            ui.deletePurchaseIdResult.setText('成功删除%d条数据' % length)

        except Exception as e:
            ui.deletePurchaseIdResult.setText(e)


class purchaseLogicInit:
    """
    会员界面逻辑
    """

    # 构造函数
    def __init__(self, ui):
        ui.addPurchaseIdEdit.editingFinished.connect(
            lambda: purchaseLogicNotificationCenter(ui, "addQueryPurchaseInformationByVIPID",
                                                    ui.addPurchaseIdEdit.text()))
        ui.purchaseAddButton.clicked.connect(
            lambda: purchaseLogicNotificationCenter(ui, "addPurchaseInformation"))

        ui.deletePurchaseIdEdit.editingFinished.connect(
            lambda: purchaseLogicNotificationCenter(ui, "deleteQueryPurchaseInformationByVIPID",
                                                    ui.deletePurchaseIdEdit.text()))
        ui.purchaseDeleteButton.clicked.connect(
            lambda: purchaseLogicNotificationCenter(ui, "deletePurchaseInformation"))
