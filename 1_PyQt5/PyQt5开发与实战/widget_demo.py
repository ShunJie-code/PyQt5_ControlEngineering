# 展示按钮的用法
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    # 1 有且只有一个对象，传入运行程序时的参数列表
    app = QApplication(sys.argv)
    # 2 创建一个窗口
    w = QWidget()
    # 3 窗口名
    w.setWindowTitle("PYQT程序")
    # 4 窗口图标
    w.setWindowIcon(QIcon('icon.jpeg'))
    # 5 窗口大小
    w.resize(500, 300)
    # 移动窗口位置
    w.move(0, 0)

    # 6 按键 两步设置父窗口
    btn = QPushButton("按键")
    btn.setParent(w)

    # 7 标签 一步设置父窗口
    label = QLabel("账号：", w)
    label.setGeometry(50, 50, 40, 30)  # x,y,w,h

    # 8 设置编辑框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(100, 50, 200, 30)

    w.show()
    app.exec()
