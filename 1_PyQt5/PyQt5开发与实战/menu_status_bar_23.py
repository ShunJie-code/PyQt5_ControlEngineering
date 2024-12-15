"""
23 菜单栏和状态栏
"""
import sys
import UI_MainWinToolbar
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = UI_MainWinToolbar.Ui_MainWindow()

    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
