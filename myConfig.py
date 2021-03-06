#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scipy.io as scio
import sys
import os


class myConfig:
    """
    配置模块
    """
    # 构造函数
    def __init__(self):
        filePath = os.path.dirname(os.path.realpath(sys.argv[0])) + '//config'
        self.fileName = filePath + '//config.mat'
        if os.path.exists(filePath) is False:
            try:
                os.makedirs(filePath)
            except Exception as e:
                print(e)
        self.config = self.loadConfig()
        self.saveConfigFunction = self.saveConfig

    def setConfigToDefault(self):
        """
        默认配置
        """
        config = {
            'purchaseMode': 1,  # 开启进货界面
            'itemsPerPage': 10,  # 货物清单界面没页显示的商品数量
        }
        return config

    def saveConfig(self):
        """
        保存配置
        """
        scio.savemat(self.fileName, self.config)

    def loadConfig(self):
        """
        加载配置
        """
        if os.path.isfile(self.fileName) is False:
            config = self.setConfigToDefault()
            # self.saveConfig()
        else:
            config = scio.loadmat(self.fileName)
            config.pop('__header__')
            config.pop('__version__')
            config.pop('__globals__')
        return config



