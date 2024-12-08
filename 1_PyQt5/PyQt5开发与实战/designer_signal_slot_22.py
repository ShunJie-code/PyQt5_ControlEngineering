"""
signal 和 slot
可以一对多
也可以多对一
"""
import sys
import UI_MainWinSignalSlot
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = UI_MainWinSignalSlot.Ui_MainWindow()

    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
