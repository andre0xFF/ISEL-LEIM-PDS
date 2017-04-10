#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt


def main():
    item_01()


def item_01_sum(n, f0, t):
    x = np.zeros(t.shape)

    for k in np.arange(1, n + 1):
        x += np.sin(2 * np.pi * (2 * k - 1) * f0 * t) / (2 * k - 1)

    x *= 4 / np.pi

    return x


def item_01():
    f0 = 1
    interval = [0, 6. / f0]
    t = np.linspace(interval[0], interval[1], 1e04)

    n = 1
    x_1 = item_01_sum(n, f0, t)

    n = 10
    x_2 = item_01_sum(n, f0, t)

    n = 10000
    x_3 = item_01_sum(n, f0, t)

    plt.figure(facecolor='w', figsize=(8, 8))

    # Subplt of 3 lines, 1 column, go to figure 1
    plt.subplot(3, 1, 1)
    plt.plot(t, x_1)

    plt.axis([interval[0], interval[1], -1.5, 1.5])
    plt.xticks(np.arange(interval[0], interval[1]+1), fontsize=12)
    plt.yticks(np.arange(-1.5, 1.6, 0.5), fontsize=12)

    plt.title('Lab1-3.1' + '\n' + r'$x(t)=\frac{4}{ \pi} \sum_{k=1}^{N}\frac{sin(2 \pi (2k-1) f_{0}t)}{2k-1}$' + '\n' + 'N = 10')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, x_2)

    plt.axis([interval[0], interval[1], -1.5, 1.5])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-1.5, 1.6, 0.5), fontsize=12)

    plt.title('N = 10')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, x_3)

    plt.axis([interval[0], interval[1], -1.5, 1.5])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-1.5, 1.5, 0.5), fontsize=12)

    plt.title('N = 10000')
    plt.grid()

    plt.tight_layout()
    plt.savefig('lab1-3.1.png', bbox_inches='tight', transparent=False)
    plt.show()


def item_02():
    pass


def item_02_function():
    pass


def item_03():
    pass


def item_03_function():
    pass


def item_04():
    pass


def item_04_function():
    pass


if __name__ == '__main__':
    main()
