#!/usr/bin/python3.5
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav


def main():
    exercise_02()


def exercise_01():

    # The step in np.arange() must be smaller than the period (T)
    t1 = np.arange(0, 2 + 1, 0.01)

    # Cos and Sin sum. Two oscillations are expected.
    x1 = np.cos(2 * np.pi * t1 + np.pi / 4) + 1 / 5 * np.sin(10 * np.pi * t1 - np.pi / 3)

    plt.plot(t1, x1)
    plt.show()

    t2 = np.arange(-2, 2 + 1, 0.01)
    x2 = np.cos(2 * np.pi * np.power(t2, 2)) + 1 / 3 * np.sin(25 * np.pi * t2)

    plt.plot(t2, x2)
    plt.show()


def exercise_02():
    # np.arange() is non inclusive (< 11)
    n = np.arange(-2, 10 + 1)
    x = np.zeros(len(n))
    x[n >= 0] = np.exp(-1 * n[n >= 0] / 5)

    plt.figure()
    plt.stem(n, x)
    plt.show()

    # Funcao escalao:
    # 1, n >= 0
    # 0, n < 0

    # n = np.arange(-10, 10)
    # x1 = np.zeros(len(n))
    # x1[(-1 * n + 3) >= 0] = 1

    # un = np.zeros(len(n))
    # un[(n + 3) >= 0] = 1
    # un1 = np.zeros(len(n))
    # un1[(-1 * n - 1) >= 0] = 1

    # x1
    n1 = np.arange(-2, 8 + 1)
    x1 = np.zeros(len(n1))
    x1[(-1 * n + 3) >= 0] = 1

    # x3
    n2 = np.arange(-5, 5 + 1)
    x3_1 = np.zeros(len(n2))
    x3_2 = np.zeros(len(n2))
    x3_1[(n + 3) >= 0] = 1
    # x3_2[(-1 * n - 1) >= 0] = 1
    x3 = x3_1

    # u2[n2 >= 1] = 1
    # x2 = u2[n2 + 3] - u2[n2 - 3]

    # x3
    # n3 = np.arange(-5, 5 + 1)
    # u3 = np.zeros(len(n3))
    # u3[n3 >= 1] = 1
    # x3 = u3[n3 + 3] + u3[-1 * n3 - 1]
    #
    # # x4
    # n4 = np.arange(-5, 25 + 1)
    # u4 = np.zeros(len(n4))
    # u4[n4 >= 1] = 1
    # x4 = np.cos(2 * np.pi * (n4 / 10)) * u4[n4] - u4 * (n4 - 20)

    figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    ax1.stem(n1, x1)
    ax2.stem(n2, x2)
    ax3.stem(n3, x3)
    ax4.stem(n4, x4)

    # this can also be done with plt.subplot
    # lines, columns, graph selection
    # plt.subplot(2, 2, 1)
    # plt.figure(2)

    plt.show()


def exercise_03():
    # soundplay > moodle
    # Discreto > Continuo: wav.write()
    # Continuo > Discreto: wav.read()

    fs, x = wav.read('pipocas11k.wav')
    plt.figure()
    plt.plot(x)

    # x[::2] begin : end : step
    s.soundPlay(x[::2], fs)

    fs = 10000
    ts = 1.0 / fs
    # Duracao que nos pretendemos
    t = np.arange(0, 3, ts)
    A = 20000
    x = A * cos(2 * np.pi * 440 * t)
    wav.write('novoficheiro.wav', fs, x)

    # Tem de ser gravado como int16:
    # wav.write('novoficheiro.wav', fs, x.astype('int16'))


if __name__ == '__main__':
    main()
