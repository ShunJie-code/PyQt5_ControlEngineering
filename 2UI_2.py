# 展示按钮的用法
import sys

from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("PYQT程序")

    btn = QPushButton("按键")

    btn.setParent(w)

    i = 1000

    print("i = {}".format(i))

    label = QLabel("账号：", w)
    # x,y,w,h
    label.setGeometry(50, 50, 40, 30)

    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(100, 50, 200, 30)

    w.show()

    app.exec()
