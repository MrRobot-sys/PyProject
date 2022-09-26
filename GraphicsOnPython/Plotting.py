import numpy as np
import matplotlib.pyplot as plt


class Graphics:
    x = np.arange(-20, 20.01, 0.01)
    xmin, xmax, ymin, ymax = -20, 20, -20, 20
    ticksFrequency = 1
    fig, ax = plt.subplots(figsize=(40, 40))
    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')
    fig.patch.set_facecolor('#ffffff')
    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
    ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
    plt.text(0.49, 0.49, r"$O$", ha='right', va='top',
             transform=ax.transAxes,
             horizontalalignment='center', fontsize=14)
    x_ticks = np.arange(xmin, xmax + 1, ticksFrequency)
    y_ticks = np.arange(ymin, ymax + 1, ticksFrequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])
    ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    def X(self, k, b):
        plt.plot(self.x, k * self.x + b)
        plt.title(r'$x$')
        plt.show()

    def AbsX(self):
        plt.plot(self.x, abs(self.x))
        plt.title(r'$|x|$')
        plt.show()

    def SqrX(self):
        plt.plot(self.x, self.x ** 2)
        plt.title(r'$x^2$')
        plt.show()

    def CubeX(self):
        plt.plot(self.x, self.x ** 3)
        plt.title(r'$x^3$')
        plt.show()

    def DivisionX(self):
        plt.plot(self.x, (1 / self.x))
        plt.title(r'$1/x$')
        plt.show()

    def SqrtX(self):
        self.x = np.arange(0.01, 20.01, 0.01)
        plt.plot(self.x, (self.x ** (1 / 2)))
        plt.title('x^(1/2)')
        plt.show()

    def ExpX(self):
        plt.plot(self.x, np.e ** self.x)
        plt.title(r'$epx^x$')
        plt.show()

    def LnX(self):
        self.x = np.arange(0.01, 20.01, 0.01)
        plt.plot(self.x, np.log(self.x))
        plt.title(r'$ln(x)$')
        plt.show()

    def SinX(self):
        plt.plot(self.x, np.sin(self.x))
        plt.title(r'$sin(x)$')
        plt.show()

    def CosX(self):
        plt.plot(self.x, np.cos(self.x))
        plt.title(r'$cos(x)$')
        plt.show()

    def TanX(self):
        plt.plot(self.x, np.tan(self.x))
        plt.title(r'$tan(x)$')
        plt.show()

    def CtgX(self):
        plt.plot(self.x, 1 / np.cos(self.x))
        plt.title(r'$ctg(x)$')
        plt.show()

    def ArcsinX(self):
        self.x = np.arange(-1, 1, 0.01)
        y = [float(i) for i in (np.arcsin(self.x))]
        plt.plot(self.x, y)
        plt.title(r'$arcsin(x)$')
        plt.show()

    def ArccosX(self):
        self.x = np.arange(-1, 1, 0.01)
        plt.plot(self.x, np.arccos(self.x))
        plt.title(r'$arccos(x)$')
        plt.show()

    def ArctgX(self):
        plt.plot(self.x, np.arctan(self.x))
        plt.title(r'$arctg(x)$')
        plt.show()

    def ArcctgX(self):
        plt.plot(self.x, np.pi / 2 - np.arctan(self.x))
        plt.title(r'$arcctg(x)$')
        plt.show()
