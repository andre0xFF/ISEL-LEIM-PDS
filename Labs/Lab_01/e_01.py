#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add graph titles, latex formulas, axis subtitles, axis best intervals


def main():
    item_05()


def item_01():
    interval = [44, 50]

    t = np.linspace(interval[0], interval[1] + 1, 1e04)
    x = 2 * np.cos(20 * np.pi * t + np.pi / 3) + np.sin(22 * np.pi * t - np.pi / 4)

    draw_graph(t, x)


def item_02():
    interval = [121, 123]

    t = np.linspace(interval[0], interval[1] + 1, 1e04)
    x = np.cos(540 * np.pi * t + np.pi / 2) + np.cos(545 * np.pi * t + np.pi / 2)

    draw_graph(t, x)


def item_03():
    interval = [31, 33]

    t = np.linspace(interval[0], interval[1] + 1, 1e04)
    x = (1 / 3 + 2 / 3 * np.cos(5 * np.pi * t)) * np.cos(100 * np.pi * t)

    draw_graph(t, x)


def item_04():
    interval = [11.2, 11.3]

    t = np.linspace(interval[0], interval[1] + 1, 1e04)
    x = np.cos(2 * np.pi * (440 + np.cos(20 * np.pi * t)))

    draw_graph(t, x)


def item_05():
    interval = [-4, 4]

    t = np.linspace(interval[0], interval[1] + 1, 1e04)
    x = np.sinc(3 * np.pi * t)

    draw_graph(t, x)


def draw_graph(t, x):
    plt.plot(t, x)
    plt.show()


if __name__ == '__main__':
    main()
