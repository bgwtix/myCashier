#!/usr/bin/python3
# -*- coding: utf-8 -*-


def VIPLogicNotificationCenter(ui, msgType, msg=None):
    """
    会员界面通知中心
    :param ui:
    :param msgType: 消息类型：
                                    "addQueryMemberInformationByVIPID"：注册会员时根据会员号查询会员信息
                                    "addNewMember"：注册会员按钮被点击
                                    "deleteQueryMemberInformationByVIPID"：注销会员时根据会员号查询会员信息
    :param msg: 输入信息，可以为空
    """
    if msgType == "addQueryMemberInformationByVIPID":  # 注册会员时根据会员号查询会员信息
        if len(msg) < 11:
            ui.addMemberIdResult.setText('卡号长度不足')
            ui.memberAddButton.setEnabled(False)
        else:
            sql = "SELECT * FROM vip WHERE vipID = %s"
            ui.myCursor.execute(sql % msg)
            myResult = ui.myCursor.fetchone()  # 查询单条
            if myResult is None:
                ui.addMemberIdResult.setText(msg)
                ui.addMemberNameEdit.setText('')
                ui.addMemberRechargeEdit.setText('')
                ui.memberAddButton.setEnabled(True)
            else:
                ui.addMemberIdResult.setText('已被注册')
                ui.addMemberNameEdit.setText(myResult['name'])
                ui.addMemberRechargeEdit.setText('')
                ui.memberAddButton.setEnabled(False)
    elif msgType == "addNewMember":  # 注册会员
        if not (ui.addMemberNameEdit.text() == '' or ui.addMemberRechargeEdit.text() == ''):
            sql = """INSERT INTO vip(vipID, integral, money, name)
                   VALUES (%s, %s, %s, "%s")"""
            val = (ui.addMemberIdResult.text(), "0", ui.addMemberRechargeEdit.text(), ui.addMemberNameEdit.text())
            try:
                ui.myCursor.execute(sql % val)
                ui.myDb.commit()
                ui.addMemberIdResult.setText('注册成功')
                ui.memberAddButton.setEnabled(False)
            except Exception as e:
                ui.addMemberIdResult.setText(e)

    elif msgType == "deleteQueryMemberInformationByVIPID":  # 注销会员时根据会员号查询会员信息
        if len(msg) < 11:
            ui.deleteMemberIdResult.setText('卡号长度不足')
            ui.memberDeleteButton.setEnabled(False)
        else:
            sql = "SELECT * FROM vip WHERE vipID = %s"
            ui.myCursor.execute(sql % msg)
            myResult = ui.myCursor.fetchone()  # 查询单条
            if myResult is None:
                ui.deleteMemberIdResult.setText('未查询到会员信息')
                ui.deleteMemberNameEdit.setText('')
                ui.deleteMemberMoneyEdit.setText('')
                ui.deleteMemberIntegralEdit.setText('')
                ui.memberDeleteButton.setEnabled(False)
            else:
                ui.deleteMemberIdResult.setText(msg)
                ui.deleteMemberNameEdit.setText(myResult['name'])
                ui.deleteMemberIntegralEdit.setText(str(myResult['integral']))
                ui.deleteMemberMoneyEdit.setText(str(myResult['money']))
                ui.memberDeleteButton.setEnabled(True)
    elif msgType == "deleteMember":  # 注销会员
        try:
            sql = "DELETE from vip where vipID=%s"
            val = ui.deleteMemberIdResult.text()
            ui.myCursor.execute(sql % val)
            ui.myDb.commit()
            ui.deleteMemberIdResult.setText('注销成功')
            ui.memberDeleteButton.setEnabled(False)
        except Exception as e:
            ui.deleteMemberIdResult.setText(e)

    elif msgType == "rechargeQueryMemberInformationByVIPID":  # 会员充值时根据会员号查询会员信息
        if len(msg) < 11:
            ui.memberRechargeResult.setText('卡号长度不足')
            ui.memberRechargeButton.setEnabled(False)
        else:
            sql = "SELECT * FROM vip WHERE vipID = %s"
            ui.myCursor.execute(sql % msg)
            myResult = ui.myCursor.fetchone()  # 查询单条
            if myResult is None:
                ui.memberRechargeResult.setText('未查询到会员信息')
                ui.memberRechargeNameEdit.setText('')
                ui.memberRechargeMoneyEdit.setText('')
                ui.memberRechargeIntegralEdit.setText('')
                ui.memberRechargeBalanceEdit.setText('')
                ui.memberRechargeButton.setEnabled(False)
            else:
                ui.memberRechargeResult.setText(msg)
                ui.memberRechargeNameEdit.setText(myResult['name'])
                ui.memberRechargeIntegralEdit.setText(str(myResult['integral']))
                ui.memberRechargeBalanceEdit.setText(str(myResult['money']))
                ui.memberRechargeButton.setEnabled(True)
    elif msgType == "memberRecharge":  # 会员充值
        if not ui.memberRechargeMoneyEdit.text() == '':
            try:
                sql = "UPDATE vip SET money=%s WHERE vipID = %s LIMIT 1"
                money = int(ui.memberRechargeBalanceEdit.text()) + int(ui.memberRechargeMoneyEdit.text())
                val = (str(money), ui.memberRechargeResult.text())
                myResult = ui.myCursor.execute(sql % val)
                if myResult == 1:
                    ui.memberRechargeBalanceEdit.setText(str(money))
                    ui.memberRechargeMoneyEdit.setText('')
                    ui.myDb.commit()
                    ui.memberRechargeResult.setText('充值成功')
                else:
                    ui.memberRechargeResult.setText('充值失败')
                ui.memberRechargeButton.setEnabled(False)
            except Exception as e:
                ui.memberRechargeResult.setText(e)


class VIPLogicInit:
    """
    会员界面逻辑
    """

    # 构造函数
    def __init__(self, ui):
        ui.addMemberIdEdit.editingFinished.connect(
            lambda: VIPLogicNotificationCenter(ui, "addQueryMemberInformationByVIPID",
                                               ui.addMemberIdEdit.text()))
        ui.memberAddButton.clicked.connect(
            lambda: VIPLogicNotificationCenter(ui, "addNewMember"))

        ui.deleteMemberIdEdit.editingFinished.connect(
            lambda: VIPLogicNotificationCenter(ui, "deleteQueryMemberInformationByVIPID",
                                               ui.deleteMemberIdEdit.text()))
        ui.memberDeleteButton.clicked.connect(
            lambda: VIPLogicNotificationCenter(ui, "deleteMember"))

        ui.memberRechargeIdEdit.editingFinished.connect(
            lambda: VIPLogicNotificationCenter(ui, "rechargeQueryMemberInformationByVIPID",
                                               ui.memberRechargeIdEdit.text()))
        ui.memberRechargeButton.clicked.connect(
            lambda: VIPLogicNotificationCenter(ui, "memberRecharge"))

