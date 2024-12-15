"""
24 主窗口
QMainWindow 菜单+工具+状态
QDialog 是对话框
QWidget 不确定窗口的用途

25 让窗口居中
"""
import sys
from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QDesktopWidget)
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        self.setWindowTitle("第一个主窗口应用")

        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage("只存在5s的消息", 5000)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./icon.jpeg'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
