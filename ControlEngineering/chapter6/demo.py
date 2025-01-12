import control as ct
# import numpy as np
import matplotlib.pyplot as plt
# 定义传递函数
num = [1]
den = [1, 1]
# sys = ct.tf(num, den)
sys = ct.tf(num, den)
# 绘制奈奎斯特图
sys_list = [sys]
ny_plt = ct.nyquist(sys_list)
print(type(ny_plt))
print(ny_plt)
print(ny_plt.lines)
# print(x.lines[0])
plt.title('Nyquist Plot')
plt.show()
lines = ny_plt.lines
# 遍历 lines 中的每个 Line2D 对象
for i, line_list in enumerate(lines):
    for j, line in enumerate(line_list):
        if line is not None:
            x_data = line.get_xdata()
            y_data = line.get_ydata()
            print(f"子图 {i+1}, 线 {j+1} 的横轴数据: {x_data}")
            print(f"子图 {i+1}, 线 {j+1} 的纵轴数据: {y_data}")
        else:
            print(f"子图 {i + 1}, 线 {j + 1} 是 None")
