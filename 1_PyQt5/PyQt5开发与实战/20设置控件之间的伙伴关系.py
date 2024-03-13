"""
键盘按住alt + a b c即可切换到不同的文本输入框
"""
import sys

import UI_MainWinBuddy

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()
    ui = UI_MainWinBuddy.Ui_MainWindow()
    # 添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
