import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.arange(-0.2, 0.3, 0.001)

    fase = 0.4 * np.pi
    fc = 440
    A = 10

    x_b = np.cos(2 * np.pi * fc * A * t)
    x_r = np.cos(2 * np.pi * fc * A * (t - 0.03))

    x_b_max = np.max(x_b)
    x_b_min = np.min(x_b)

    plt.plot(t, x_b)
    plt.plot(t, x_r)
    plt.show()


if __name__ == '__main__':
    main()
