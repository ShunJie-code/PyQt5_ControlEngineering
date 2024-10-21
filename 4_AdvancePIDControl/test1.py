import numpy as np
import matplotlib.pyplot as plt
from control import tf, rlocus
import time

# 定义系统传递函数
num = [1]
den = [1, 2, 2, 1]
sys = tf(num, den)

# 绘制根轨迹
rlocus(sys)


def onpick(event):
    print("Event triggered!")
    # 进一步处理事件的代码


fig = plt.gcf()
print('hello')
plt.show()
time.sleep(1)  # 等待 1 秒，确保图形窗口显示并可交互
fig.canvas.mpl_connect('pick_event', onpick)