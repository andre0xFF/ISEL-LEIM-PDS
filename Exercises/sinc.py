#!/usr/bin/python3.5


import numpy as np
import matplotlib.pyplot as plt


def main():
    t = np.arange(-5, 5, 0.1)

    # sinc function or np.sinc(t)
    # x = np.sin(np.pi * t) / (np.pi * t)
    x = np.sinc(t)

    plt.xlabel('sinc(t)')
    plt.ylabel('Intensity')
    plt.axis([-5, 5, -.25, 1.25])
    plt.grid()
    plt.plot(t, x)
    plt.show()


if __name__ == '__main__':
    main()
