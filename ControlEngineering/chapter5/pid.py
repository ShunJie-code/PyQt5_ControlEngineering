"""垂直驱动机械臂模型"""
# 方法1 添加到系统路径
# import sys
# sys.path.append('../chapter4')
# from PredefinedFunction import *

# 方法2，将文件夹定义为包，通过包来引用
# 建议用包引用，并且使用绝对路径导入其他文件夹下python文件
from ControlEngineering.chapter4.PredefinedFunction import *
from control.matlab import *

g = 9.81
length = 0.2
m = 0.5
mu = 1.5e-2
J = 1.0e-2

p = tf([0, 1], [J, mu, m * g * length])
ref = 30
kp = (0.5, 1, 2)


def test1():
    ls = line_style_generator()
    print(' 123')
    hi()


if __name__ == '__main__':
    test1()
