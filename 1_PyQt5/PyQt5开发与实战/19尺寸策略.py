"""
期望尺寸
不同的控件有不同的期望尺寸，用户不可修改
"""
import sys

import UI_MainWinSizePolicy

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()
    ui = UI_MainWinSizePolicy.Ui_MainWindow()
    # 添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
