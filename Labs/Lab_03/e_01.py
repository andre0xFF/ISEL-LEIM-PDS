import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt


def main():
    item_a()
    item_c()


def item_a():
    "b) corta banda"
    b = ss.firwin(101, [0.1, 0.9])
    w, h = ss.freqz(b)
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.show()


def item_c():
    n = np.arange(50)
    x = 10 + 2 * np.cos((np.pi / 6) * n) + 10 * np.cos((np.pi / 3) * n)
    y = system(1, 0.9, x)

    plt.figure()
    plt.xlabel('x')
    plt.ylabel('r')
    plt.title('b = 1; r = 0.9')
    plt.plot(y)
    plt.show()


def system(b, r, x):
    b1 = np.array([1])
    a1 = np.zeros([b + 1])
    a1[0] = 1
    a1[-1] = r

    return ss.lfilter(b1, a1, x)

if __name__ == "__main__":
    main()
