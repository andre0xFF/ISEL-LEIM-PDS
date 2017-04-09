#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt


def main():
    item_01()
    item_02()
    item_03()
    item_04()
    item_05()


def item_01():
    # Array that contains "area" of the graphic we want to plot
    interval = [44, 50]

    # Creates an array of evenly spaced numbers in designated range
    t = np.linspace(interval[0], interval[1] + 1, 1e04)

    # Wave function
    x = 2 * np.cos(20 * np.pi * t + np.pi / 3) + np.sin(22 * np.pi * t - np.pi / 4)

    # Closes previous plots
    plt.close('all')

    # Creates figure of the graphic with the determined size and color
    plt.figure(facecolor='w')

    # Plot the graph
    plt.plot(t, x)

    # Selects the axis to be displayed in the graphic
    plt.axis([interval[0], interval[1], -3.5, 3.5])

    # Determines the ticks axis range and size
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-3.5, 3.6), fontsize=12)

    # Formats the graphic with axis names, text labels, and with various informations of the wave being analyzed
    plt.xlabel('t(s)', fontsize=15)
    plt.ylabel('x(t)', fontsize=15)
    plt.title('Lab-1 1.1' + '\n' + r'$x(t)=2\cos \left(20 \pi t + \frac{\pi}{3} \right) +  \sin \left(22\pi t- \frac{\pi}{4}\right)$')

    # Enables the graphic grid display
    plt.grid()

    # Saves graphic image
    plt.savefig('lab1_1.1.png', bbox_inches='tight', transparent=False)

    # Displays created Graphic
    plt.show()


def item_02():
    interval = [121, 123]
    t = np.linspace(interval[0], interval[1] + 1, 1e03)
    x = np.cos(540 * np.pi * t + np.pi / 2) + np.cos(545 * np.pi * t + np.pi / 2)

    plt.close('all')

    plt.figure(facecolor='w')
    plt.plot(t, x, 'm')

    plt.axis([interval[0], interval[1], -2, 2])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-2, 3), fontsize=12)
    plt.xlabel('t(s)', fontsize=15)
    plt.ylabel('x(t)', fontsize=15)
    plt.title('Lab-1 1.2' + '\n' + r'$x(t)=\cos \left(540 \pi t + \frac{\pi}{2} \right) + \cos \left(545\pi t- \frac{\pi}{2}\right)$')

    plt.grid()
    plt.savefig("lab1_1.2.png", bbox_inches='tight', transparent=False)
    plt.show()


def item_03():
    interval = [31, 33]
    t = np.linspace(interval[0], interval[1], 1e04)
    x = (1 / 3 + 2 / 3 * np.cos(5 * np.pi * t)) * np.cos(100 * np.pi * t)

    plt.close('all')

    plt.figure(facecolor='w')
    plt.plot(t, x, 'r')

    plt.axis([interval[0], interval[1], -1.2, 1.2])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-1.2, 1.8), fontsize=12)

    plt.xlabel('t(s)', fontsize=15)
    plt.ylabel('x(t)', fontsize=15)
    plt.title('Lab-1 1.3' + '\n' + r'$x(t)=\left(\frac{1}{3} +\frac{2}{3}\cos \left(5 \pi t \right)\right) \times  \cos \left(100\pi t\right)$')

    plt.grid()
    plt.savefig("lab1_1.3.png", bbox_inches='tight', transparent=False)
    plt.show()


def item_04():
    interval = [11.2, 11.3]
    t = np.linspace(interval[0], interval[1], 1e04)
    x = np.cos(2 * np.pi * t * (440 + np.cos(20 * np.pi * t)))

    plt.close('all')
    plt.figure(facecolor='w')
    plt.plot(t, x)

    plt.axis([interval[0], interval[1], -1.2, 1.2])
    plt.xlabel('t(s)', fontsize=12)
    plt.ylabel('x(t)', fontsize=12)
    plt.title('Lab-1 1.4' + '\n' + r'$x(t)=\cos \left(2 \pi t  \left( 440 + \cos \left(20 \pi t \right) \right) \right)$')

    plt.grid()
    plt.savefig("lab1_1.4.png", bbox_inches='tight', transparent=False)
    plt.show()


def item_05():
    interval = [-4, 4]
    t = np.linspace(interval[0], interval[1], 1e04)
    # x = np.sinc(3 * np.pi * t)
    # x = np.sin(3*np.pi*t)/(3*np.pi*t)
    x = np.sinc(3 * t)

    plt.close('all')
    plt.figure(facecolor='w')
    plt.plot(t, x)

    plt.axis([interval[0], interval[1], -0.3, 1.1])
    plt.xlabel('t(s)', fontsize=12)
    plt.ylabel('x(t)', fontsize=12)
    plt.title('Lab-1 1.5' + '\n' + r'$x(t)=\frac{\sin\left(3 \pi t\right)}{3 \pi t}$')

    plt.grid()
    plt.savefig("lab1_1.5.png", bbox_inches='tight', transparent=False)
    plt.show()


if __name__ == '__main__':
    main()
