"""
预定义三个函数
4.1 绘图时，确定的线型生成器
4.2 完善绘图的函数
4.3 完善伯德图函数
"""


def line_style_generator():
    line_style = ['-', '--', '-.', ':']
    line_id = 0
    while True:
        yield line_style[line_id]
        line_id = (line_id + 1) % len(line_style)


def plot_set(fig_ax, *args):
    fig_ax.set_xlabel(args[0])  # 通过参数1设置x轴标签
    fig_ax.set_ylabel(args[1])  # 通过参数2设置y轴标签
    fig_ax.grid(ls=':')
    if len(args) == 3:
        fig_ax.legend(loc=args[2])  # 通过参数3设置图例的位置


def bode_plot_set(fig_ax, *args):
    # 设置幅频图的网格和y轴的标签
    fig_ax[0].grid(which='both', ls=':')
    fig_ax[0].set_ylabel('Gain [dB]')

    # 设置相频图的网格和x、y轴标签
    fig_ax[1].grid(which='both', ls=':')
    fig_ax[1].set_xlabel('$\omega$ [rad/s]')
    fig_ax[1].set_ylabel('Phase [deg]')

    if len(args) > 0:
        fig_ax[1].legend(loc=args[1])
    if len(args) > 1:
        fig_ax[0].legend(loc=args[1])
