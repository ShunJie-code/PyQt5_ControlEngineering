print("asd")
from pylab import mpl
from control import tf


# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"] # 黑体
# 设置正常符号显示
mpl.rcParams["axes.unicode_minus"] = False
# %matplotlib widget 日期设置为简洁格式
mpl.rcParams['date.converter'] = 'concise'
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6), dpi=80)
ts = 0.25                     #
p = tf(1, [10, 2, 0])
d_p = c2d(p, ts, 'zoh')
rlocus(d_p)
# plt.ion()
print("hello")
plt.show()
# plt.close()
