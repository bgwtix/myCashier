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
    连接到数据库
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
        Widget_init.__init__(self)
        self.myDb, self.myCursor = connectMySQL()
        if self.myDb is None:
            QMessageBox.question(self, '错误', '连接服务器失败',
                                 QMessageBox.Yes, QMessageBox.Yes)
            quit(1)

    def closeEvent(self, event):
        """

        :param event:
        """
        print('close')
        if 1:
            reply = QMessageBox.question(self, '信息', '确认退出吗？',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                self.myCursor.close()
                self.myDb.close()
                event.accept()
            else:
                event.ignore()
        print('close done')


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
