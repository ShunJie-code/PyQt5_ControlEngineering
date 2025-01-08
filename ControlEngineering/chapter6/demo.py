import control as ct
import numpy as np
import matplotlib.pyplot as plt
# 定义传递函数
num = [1]
den = [1, 1]
sys = ct.tf(num, den)
# 绘制奈奎斯特图
x = ct.nyquist(sys)
print(type(x))
print()
plt.title('Nyquist Plot')
plt.show()