#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from cashierUI import Widget_init
import MySQLdb
from myConfig import myConfig
from PyQt5.QtCore import Qt, QPoint


def connectMySQL():
    """
    连接到数据库,如果要使用的表不存在则创建
    :return: myDb， myCursor
    """
    try:
        myDb = MySQLdb.connect(
            host='localhost',
            user='Skyrim',
            passwd='123456789',
            database="myCashier",
            charset='utf8',
        )
        myCursor = myDb.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = 'show tables like "cashier"'
        if not myCursor.execute(sql):
            sql = ("CREATE TABLE cashier (goodsID INT"  # 序号
                   ", price FLOAT"  # 售价
                   ", Discount FLOAT"  # 折扣-保留参数
                   ", purchasePrice FLOAT"  # 进价-仅管理员可见
                   ", stock INT"  # 当前库存
                   ", accumulativeTotal INT"  # 累计进货量
                   ", remarks VARCHAR(255))"  # 货物说明
                   )
            myCursor.execute(sql)
        sql = 'show tables like "vip"'
        if not myCursor.execute(sql):
            sql = ("CREATE TABLE vip (vipID BIGINT "  # 序号
                   ", integral INT"  # 积分
                   ", money  INT"  # 余额
                   ", name VARCHAR(10))"  # 货物说明
                   )
            myCursor.execute(sql)

    except Exception as e:
        print(e)
        myDb = None
        myCursor = None

    return myDb, myCursor


class myCashier(Widget_init, myConfig):
    """
    是
    """
    def __init__(self):
        myConfig.__init__(self)
        self.myDb, self.myCursor = connectMySQL()
        Widget_init.__init__(self)
        if self.myDb is None:
            QMessageBox.about(self, '错误', '连接服务器失败')
            quit(1)

    def closeEvent(self, event):
        """

        :param event:
        """
        reply = QMessageBox.question(self, '信息', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.myCursor.close()
            self.myDb.close()
            event.accept()
        else:
            event.ignore()


def gui_main(maxFlag=0):
    """
    启动hui界面
    :param maxFlag:  界面最大化显示标志：
                                          0： 直接显示(默认)
                                        非0： 最大化显示
    """
    app = QApplication(sys.argv)
    ex = myCashier()
    if maxFlag:
        ex.showMaximized()  # 界面最大化显示
    else:
        ex.show()  # 界面显示
    sys.exit(app.exec_())


if __name__ == '__main__':
    gui_main()
