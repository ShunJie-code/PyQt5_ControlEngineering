import matplotlib.pyplot as plt
import control

# 定义 PID 控制器的传递函数
Kp = 1.0
Ki = 0.5
Kd = 0.2
num = [Kd, Kp, Ki]
den = [1, 0]
pid_tf = control.tf(num, den)
gs = control.tf([0, 2], [6, 5, 1])
control.feedback(pid_tf * gs, 1)
# 绘制伯德图
omega, mag, phase = control.bode(pid_tf)

plt.figure()
plt.subplot(211)
plt.semilogx(omega, mag)
plt.title('Bode Plot of PID Controller')
plt.ylabel('Magnitude (dB)')
plt.grid(which='both')

plt.subplot(212)
plt.semilogx(omega, phase)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (deg)')
plt.grid(which='both')

plt.show()
