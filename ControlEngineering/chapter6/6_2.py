import control as ct
import numpy as np
import matplotlib.pyplot as plt

sys_tt = ct.tf([1], [1, 2, 1])
T = np.linspace(0, 10, 100)  # 从0到10秒，共100个时间点
U = np.sin(T)  # 例如，使用正弦波作为输入
# X0 = 0  # 初始状态，对于简单系统可以是0
t, y = ct.forced_response(sys_tt, T, U)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('System Response')
plt.show()
