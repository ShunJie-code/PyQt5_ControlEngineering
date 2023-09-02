# 展示按钮的用法
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    # 有且只有一个对象，传入运行程序时的参数列表
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 窗口名
    w.setWindowTitle("PYQT程序")
    w.setWindowIcon(QIcon('icon.jpeg'))
    # 两步设置按键父窗口
    btn = QPushButton("按键")
    btn.setParent(w)

    i = 1000

    print("i = {}".format(i))

    # 一步设置标签的父窗口
    label = QLabel("账号：", w)
    # x,y,w,h
    label.setGeometry(50, 50, 40, 30)

    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(100, 50, 200, 30)
    # 窗口大小
    w.resize(500, 300)
    w.show()

    app.exec()
