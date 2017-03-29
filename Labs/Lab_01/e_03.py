#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add graph titles, latex formulas, axis subtitles, axis best intervals

# TODO: Draw 3 subplots for the following:
# n = 1
# n = 10
# n = 10000


def main():
    pass


def item_01_function(interval, n, f0):
    x = np.zeros(len(interval))

    for k in np.arange(interval[0], interval[1] + 1):
        x = x + 4 / np.pi * (np.sin(2 * np.pi * (2 * k - 1) * f0 * t) / (2 * k - 1))

    return x

def item_01():
    f0 = 1
    interval = [0, 6 / f0]
    t = np.linspace(interval[0], interval[1], 1e04)

    n = 1
    x_1 = item_01_function(interval, n, f0)

    n = 10
    x_2 = item_01_function(interval, n, f0)

    n = 10000
    x_3 = item_01_function(interval, n, f0)

    # Subplot of 3 lines and 1 column
    figure, (ax1, ax2, ax3) = plt.subplots(3, 1)

    ax1.plot(t, x_1)
    ax2.plot(t, x_2)
    ax3.plot(t, x_3)
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
