"""
绝对布局：控件不再任何固有的布局中，位置和大小可以随意修改
"""
import sys

import UI_MainWinContainLayout

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()
    ui = UI_MainWinContainLayout.Ui_MainWindow()
    # 添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
