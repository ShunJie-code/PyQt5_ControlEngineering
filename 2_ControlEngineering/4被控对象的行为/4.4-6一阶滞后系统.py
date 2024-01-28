from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from PredefinedFunction import *

T = 0.5
K = 1
P = tf([0, K], [T, 1])
y, t = step(P, np.arange(0, 5, 0.01))

fig, ax = plt.subplots()
ax.plot(t, y)
plot_set(ax, 't', 'y')

plt.show()
