# -*- coding: utf-8 -*-

"""

Created on Fri Apr 26 20:49:32 2019



@author: Tiny

"""

# =============================================================================

''' 鼠标事件，各动作响应事件可以随意自定义'''

''' 参考: 1. https://blog.csdn.net/richenyunqi/article/details/80554257

             pyqt判断鼠标点击事件——左键按下、中键按下、右键按下、左右键同时按下等等;

          2. https://fennbk.com/8065

             Pyqt5 之 鼠标 (事件与方法介绍)

          3. https://blog.csdn.net/leemboy/article/details/80462632

             PyQt5编程-鼠标事件

          4. https://doc.qt.io/qtforpython/PySide2/QtGui/QWheelEvent.html#PySide2.QtGui.PySide2.QtGui.QWheelEvent.delta

             QWheelEvent'''

# =============================================================================

# =============================================================================

''' PyQt4 和 PyQt5区别：'''

#   PySide2.QtGui.QWheelEvent.delta()

#   Return type:	int

#   This function has been deprecated, use pixelDelta() or angleDelta() instead.

# =============================================================================

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import *

from PyQt5.QtCore import *

import sys

'''自定义的QLabel类'''


class myImgLabel(QtWidgets.QLabel):

    def __init__(self, parent=None):

        super(myImgLabel, self).__init__(parent)

        f = QFont("ZYSong18030", 10)  # 设置字体,字号

        self.setFont(f)  # 未来自定义事件后，该两句删掉或注释掉

    '''重载一下鼠标按下事件(单击)'''

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下

            self.setText("单击鼠标左键的事件: 自己定义")

            print("单击鼠标左键")  # 响应测试语句

        elif event.buttons() == QtCore.Qt.RightButton:  # 右键按下

            self.setText("单击鼠标右键的事件: 自己定义")

            print("单击鼠标右键")  # 响应测试语句

        elif event.buttons() == QtCore.Qt.MidButton:  # 中键按下

            self.setText("单击鼠标中键的事件: 自己定义")

            print("单击鼠标中键")  # 响应测试语句

        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:  # 左右键同时按下

            self.setText("同时单击鼠标左右键的事件: 自己定义")

            print("单击鼠标左右键")  # 响应测试语句

        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton:  # 左中键同时按下

            self.setText("同时单击鼠标左中键的事件: 自己定义")

            print("单击鼠标左中键")  # 响应测试语句

        elif event.buttons() == QtCore.Qt.MidButton | QtCore.Qt.RightButton:  # 右中键同时按下

            self.setText("同时单击鼠标右中键的事件: 自己定义")

            print("单击鼠标右中键")  # 响应测试语句

        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton \
 \
                | QtCore.Qt.RightButton:  # 左中右键同时按下

            self.setText("同时单击鼠标左中右键的事件: 自己定义")

            print("单击鼠标左中右键")  # 响应测试语句


    '''重载一下滚轮滚动事件'''


    def wheelEvent(self, event):
        #        if event.delta() > 0:                                                 # 滚轮上滚,PyQt4

        # This function has been deprecated, use pixelDelta() or angleDelta() instead.

        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度

        angleX = angle.x()  # 水平滚过的距离(此处用不上)

        angleY = angle.y()  # 竖直滚过的距离

        if angleY > 0:

            self.setText("滚轮向上滚动的事件: 自己定义")

            print("鼠标滚轮上滚")  # 响应测试语句

        else:  # 滚轮下滚

            self.setText("滚轮向下滚动的事件: 自己定义")

            print("鼠标滚轮下滚")  # 响应测试语句


    '''重载一下鼠标双击事件'''


    def mouseDoubieCiickEvent(self, event):
        #        if event.buttons () == QtCore.Qt.LeftButton:                           # 左键按下

        #            self.setText ("双击鼠标左键的功能: 自己定义")

        self.setText("鼠标双击事件: 自己定义")


    '''重载一下鼠标键释放事件'''


    def mouseReleaseEvent(self, event):
        self.setText("鼠标释放事件: 自己定义")

        print("鼠标释放")  # 响应测试语句


    '''重载一下鼠标移动事件'''


    def mouseMoveEvent(self, event):
        self.setText("鼠标移动事件: 自己定义")

        print("鼠标移动")  # 响应测试语句


    #    '''重载一下鼠标进入控件事件'''

    #    def enterEvent(self, event):

    #

    #

    #    '''重载一下鼠标离开控件事件'''

    #    def leaveEvent(self, event):

    #


'''定义主窗口'''


class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.imgLabel = myImgLabel()  # 声明imgLabel

        self.image = QImage()  # 声明新img

        if self.image.load("image/cc2.png"):  # 如果载入图片,则

            self.imgLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片

        self.gridLayout = QtWidgets.QGridLayout(self)  # 布局设置

        self.gridLayout.addWidget(self.imgLabel, 0, 0, 1, 1)  # 注释掉这两句,则不显示图片


'''主函数'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myshow = MyWindow()

    myshow.show()

    sys.exit(app.exec_())