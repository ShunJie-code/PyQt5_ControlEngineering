"""
获取 nyquist 图坐标数据
"""
import control as ct
import matplotlib.pyplot as plt

# 1 定义传递函数
num = [1]
den = [1, 1]
sys = ct.tf(num, den)

# 2 绘制奈奎斯特图
sys_list = [sys]
# ny_plt = ct.nyquist(sys_list, plot=False)  # 这一句ny_plt = 0
ny_plt = ct.nyquist(sys_list)
# print(1, type(ny_plt))
# print(2, ny_plt)


# 3 遍历 lines 中的每个 Line2D 对象，获取曲线坐标数据
lines = ny_plt.lines
for i, line_list in enumerate(lines):
    for j, line in enumerate(line_list):
        if line is not None:
            x_data = line.get_xdata()
            y_data = line.get_ydata()
            print(f"子图 {i+1}, 线 {j+1} 的横轴数据: {x_data}")
            print(f"子图 {i+1}, 线 {j+1} 的纵轴数据: {y_data}")
        else:
            print(f"子图 {i + 1}, 线 {j + 1} 是 None")
plt.show()  # 阻塞函数
