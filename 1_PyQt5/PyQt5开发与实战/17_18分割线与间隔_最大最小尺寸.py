import sys

import UI_MainWinSpacerLine

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()
    ui = UI_MainWinSpacerLine.Ui_MainWindow()
    # 添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
