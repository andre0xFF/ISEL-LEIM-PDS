#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add graph titles, latex formulas, axis subtitles, axis best intervals


def main():
    item_01()


def item_01():
    interval = [-4.5, 1.5]
    t = np.linspace(interval[0], interval[1] + 1, 1e04)
    x = np.zeros(len(t))

    x[(-2 * t - 4 >= 0) & (-t - 4)] = 1

    # plt.close()
    # plt.figure(facecolor='w', figsize=(7, 5))
    # plt.plot(t, x, 'k', linewidth=1.5)
    # plt.axis([interval[0], interval[1], -0.1, 1.1]])
    # plt.xticks()
    # plt.yticks()
    # plt.title(r'$x(t)=u(-2t-4)-u(-t-4))
    # plt.xlabel()
    plt.grid()
    plt.show()
    # plt.savefig()


def item_02():
    pass


def item_03():
    pass


if __name__ == '__main__':
    main()
