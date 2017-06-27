import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt


def main():
    item_a()
    item_b()
    item_c()
    item_d()


def item_a():
    filter(1 / 3, True, 'hamming')


def item_b():
    filter(1 / 3, False, 'hamming')


def item_c():
    filter([1 / 4, 1 / 3], False, 'hamming')


def filter(wc, pass_zero, window):
    y = ss.firwin(101, wc, pass_zero=pass_zero, window=window)
    w, h = ss.freqz(y)

    plt.figure()
    plt.plot(w, abs(h))
    plt.show()


def item_d():
    y = ss.firwin(101, 1 / 4, pass_zero=False, window='blackman')
    w, h = ss.freqz(y)

    plt.figure()
    plt.plot(w, 20 * np.log(abs(h)))
    plt.show()


if __name__ == "__main__":
    main()
