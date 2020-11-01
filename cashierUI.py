#!/usr/bin/python3
# -*- coding: utf-8 -*-

from checkOutUI import *
from VIPUI import *
from inventoryUI import *
from purchaseUI import *
from configUI import configUIInit
from checkOutLogic import checkOutLogicInit
from VIPLogic import VIPLogicInit
from purchaseLogic import purchaseLogicInit
from configLogic import configLogicInit
from inventoryLogic import inventoryLogicInit


class Widget_init(checkOutUIInit, VIPUIInit, inventoryUIInit, purchaseUIInit, configUIInit):
    """
    1
    """

    # 构造函数
    def __init__(self):
        checkOutUIInit.__init__(self)
        VIPUIInit.__init__(self)
        inventoryUIInit.__init__(self)
        purchaseUIInit.__init__(self)
        configUIInit.__init__(self)

        # self.VIPIdText.installEventFilter(self)
        # self.checkOutInputIDText.installEventFilter(self)

        self.insertTab(0, self.checkOutTab, "收银系统")
        self.insertTab(1, self.VIPTab, "会员系统")
        self.insertTab(2, self.inventoryTab, "货物清单")
        self.insertTab(3, self.purchaseTab, "进货系统")
        self.insertTab(4, self.configTab, "设置")

        checkOutLogicInit(self)
        VIPLogicInit(self)
        inventoryLogicInit(self)
        purchaseLogicInit(self)
        configLogicInit(self)

        self.setWindowTitle('收银系统')

        self.setMinimumSize(940, 400)

    # def eventFilter(self, obj, event):
    #     """
    #     运行会变慢
    #     :param obj:
    #     :param event:
    #     :return:
    #     """
    #     if obj == self.VIPIdText:
    #         if event.type() == QEvent.FocusIn:
    #             if obj.text().strip() == '请输入会员卡号':
    #                 obj.clear()
    #         elif event.type() == QEvent.FocusOut:
    #             if obj.text().strip() == '':
    #                 obj.setText("请输入会员卡号")
    #         return False
    #     if obj == self.checkOutInputIDText:
    #         if event.type() == QEvent.FocusIn:
    #             if obj.text().strip() == '请输入商品号':
    #                 obj.clear()
    #         elif event.type() == QEvent.FocusOut:
    #             if obj.text().strip() == '':
    #                 obj.setText("请输入商品号")
    #         return False
    #     return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget_init()
    # ex.showMaximized()   #界面最大化显示
    ex.show()  # 界面显示
    sys.exit(app.exec_())
