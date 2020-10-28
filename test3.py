import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class SplitterExample(QWidget):
    """
    2
    """
    def __init__(self):
        super(SplitterExample, self).__init__()
        self.initUI()

    def initUI(self):
        """
        2
        """
        # 设置全局布局为水平布局，设置标题与初始大小窗口
        hbox = QHBoxLayout()
        self.setWindowTitle("QSplitter例子")
        self.setGeometry(300, 300, 300, 200)
        # 实例化QFrame控件
        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        # 实例化QSplitter控件并设置初始为水平方向布局
        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        # 向Splitter内添加控件。并设置游戏的初始大小
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])
        # 实例化Splitter管理器，添加控件到其中，设置垂直方向
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        # 设置窗体全局布局以及子布局的添加
        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SplitterExample()
    demo.show()
    sys.exit(app.exec_())
