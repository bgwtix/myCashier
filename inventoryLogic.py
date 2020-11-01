#!/usr/bin/python3
# -*- coding: utf-8 -*-
import scipy.io as scio
import sys
import os
import math
from PyQt5.QtWidgets import *


def inventoryWidgetUpdata(ui):
    """

    :param ui:
    """
    ui.pageLabel.setText('%d/%d' % (ui.currentPage, ui.totalPage))
    itemOffset = (ui.currentPage - 1) * ui.itemsPerPage
    sql = "SELECT * FROM cashier ORDER BY %s ASC LIMIT %d OFFSET %d"
    val = ('goodsID', ui.itemsPerPage, itemOffset)
    ui.myCursor.execute(sql % val)
    myResult = ui.myCursor.fetchone()
    rowCnt = 0
    ui.inventoryWidget.clearContents()
    while myResult is not None:
        ui.inventoryWidget.setItem(rowCnt, 0,
                                   QTableWidgetItem(str(myResult['goodsID'])))
        ui.inventoryWidget.setItem(rowCnt, 1,
                                   QTableWidgetItem(str(myResult['remarks'])))
        ui.inventoryWidget.setItem(rowCnt, 2,
                                   QTableWidgetItem(str(myResult['price'])))
        ui.inventoryWidget.setItem(rowCnt, 3,
                                   QTableWidgetItem(str(myResult['stock'])))
        ui.inventoryWidget.setItem(rowCnt, 4,
                                   QTableWidgetItem(str(myResult['accumulativeTotal'])))
        rowCnt += 1
        myResult = ui.myCursor.fetchone()


def inventoryLogicNotificationCenter(ui, msgType, msg=None):
    """

    :param ui:
    :param msgType:
    :param msg:
    """
    if msgType == 'firstPageButton':
        if ui.totalPage:
            ui.currentPage = 1
            inventoryWidgetUpdata(ui)
    elif msgType == 'inventorySearchButton':
        sql = 'SELECT * FROM cashier'
        totalItems = ui.myCursor.execute(sql)
        ui.totalPage = math.ceil(totalItems / ui.itemsPerPage)
        if ui.totalPage:
            ui.currentPage = 1
            inventoryWidgetUpdata(ui)
    elif msgType == 'nextPageButton':
        if ui.currentPage < ui.totalPage:
            ui.currentPage += 1
            inventoryWidgetUpdata(ui)
    elif msgType == 'previousPageButton':
        if ui.currentPage > 1:
            ui.currentPage -= 1
            inventoryWidgetUpdata(ui)
    elif msgType == 'lastPageButton':
        if ui.currentPage < ui.totalPage:
            ui.currentPage = ui.totalPage
            inventoryWidgetUpdata(ui)
    elif msgType == 'gotoEditPageButton':
        if ui.pageEdit.text().isnumeric():
            pageNum = int(ui.pageEdit.text())
            if pageNum and pageNum <= ui.totalPage:
                ui.currentPage = pageNum
                inventoryWidgetUpdata(ui)


class inventoryLogicInit:
    """
    货物清单界面逻辑
    """

    # 构造函数
    def __init__(self, ui):
        ui.firstPageButton.clicked.connect(
            lambda: inventoryLogicNotificationCenter(ui, "firstPageButton"))
        ui.inventorySearchButton.clicked.connect(
            lambda: inventoryLogicNotificationCenter(ui, "inventorySearchButton"))
        ui.nextPageButton.clicked.connect(
            lambda: inventoryLogicNotificationCenter(ui, "nextPageButton"))
        ui.previousPageButton.clicked.connect(
            lambda: inventoryLogicNotificationCenter(ui, "previousPageButton"))
        ui.lastPageButton.clicked.connect(
            lambda: inventoryLogicNotificationCenter(ui, "lastPageButton"))
        ui.gotoEditPageButton.clicked.connect(
            lambda: inventoryLogicNotificationCenter(ui, "gotoEditPageButton", ui.pageEdit.text()))
