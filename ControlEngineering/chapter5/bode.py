import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def transfer_function(w):
    s = 1j * w
    return np.abs(1 / (s + 1)), np.angle(1 / (s + 1))


class BodePlotCanvas():
    def __init__(self, parent=None):
        # 创建一个 matplotlib 的 Figure 对象
        fig, self.ax = plt.subplots(2, 1, figsize=(8, 6))
        super().__init__(fig)
        # self.setParent(parent)

    def plot_bode(self, tf):
        # 设置频率范围
        w = np.logspace(-2, 4, 1000)
        # 计算频率响应
        mag, phase = tf(w)
        # 绘制幅度图
        self.ax[0].semilogx(w, 20 * np.log10(mag))
        self.ax[0].set_title('Bode Magnitude Plot')
        self.ax[0].set_xlabel('Frequency (rad/s)')
        self.ax[0].set_ylabel('Magnitude (dB)')
        # 绘制相位图
        self.ax[1].semilogx(w, phase * 180 / np.pi)
        self.ax[1].set_title('Bode Phase Plot')
        self.ax[1].set_xlabel('Frequency (rad/s)')
        self.ax[1].set_ylabel('Phase (degrees)')
        # 自动调整子图布局
        self.fig.tight_layout()
        # 刷新画布
        self.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建一个垂直布局
        layout = QVBoxLayout()
        # 创建图形画布
        self.canvas = BodePlotCanvas(self)
        layout.addWidget(self.canvas)
        # 创建一个中心部件并设置布局
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    window.canvas.plot_bode(transfer_function)
    app.exec_()
