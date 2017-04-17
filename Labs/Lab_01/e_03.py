#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt


def main():
    item_01()
    item_02()
    item_03()
    item_04()


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
    plt.savefig('lab1_3.1.png', bbox_inches='tight', transparent=False)
    plt.show()


def item_02_sum(n, f0, t):
    x = np.zeros(t.shape)

    for k in np.arange(1, n + 1):
        x += (np.sin( np.pi * k / 4 ) / ( np.pi * k / 4 ))*np.cos(2*np.pi*k*f0*t)

    x +=-1 

    return x

def item_02():
    f0 = 1
    interval = [0, 6. / f0]
    t = np.linspace(interval[0], interval[1], 1e04)

    n = 1
    x_1 = item_02_sum(n, f0, t)

    n = 10
    x_2 = item_02_sum(n, f0, t)

    n = 10000
    x_3 = item_02_sum(n, f0, t)

    plt.figure(facecolor='w', figsize=(8, 8))

    # Subplt of 3 lines, 1 column, go to figure 1
    plt.subplot(3, 1, 1)
    plt.plot(t, x_1)

    plt.axis([interval[0], interval[1], -2, 0.1])
    plt.xticks(np.arange(interval[0], interval[1]+1), fontsize=12)
    plt.yticks(np.arange(-2, 0.1, 0.5), fontsize=12)
    
    plt.title('Lab1-3.2' + '\n' + r'$x(t)=-1+\sum_{k=1}^{N}\frac{\sin\left(\pi/4\right)}{\pi k/4}\cos\left(2 \pi k f_{0} t \right)$' + '\n' + 'N = 1')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, x_2)

    plt.axis([interval[0], interval[1], -2, 1])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-2, 1.1, 0.5), fontsize=12)

    plt.title('N = 10')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, x_3)

    plt.axis([interval[0], interval[1], -2, 1])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-2, 1.1, 0.5), fontsize=12)

    plt.title('N = 10000')
    plt.grid()

    plt.tight_layout()
    plt.savefig('lab1_3.2.png', bbox_inches='tight', transparent=False)
    plt.show()


def item_03_sum(n, f0, t):
    x = np.zeros(t.shape)

    for k in np.arange(1, n + 1):
        x += np.sin( 2 * np.pi * k * f0 * t )/k

    x *= 2 / np.pi    

    return x

def item_03():
    f0 = 1
    interval = [0, 6. / f0]
    t = np.linspace(interval[0], interval[1], 1e04)

    n = 1
    x_1 = item_03_sum(n, f0, t)

    n = 10
    x_2 = item_03_sum(n, f0, t)

    n = 10000
    x_3 = item_03_sum(n, f0, t)

    plt.figure(facecolor='w', figsize=(8, 8))

    # Subplt of 3 lines, 1 column, go to figure 1
    plt.subplot(3, 1, 1)
    plt.plot(t, x_1)

    plt.axis([interval[0], interval[1], -1, 1])
    plt.xticks(np.arange(interval[0], interval[1]+1), fontsize=12)
    plt.yticks(np.arange(-1, 1.1, 0.5), fontsize=12)
    
    plt.title('Lab1-3.3' + '\n' + r'$x(t)=\frac{2}{ \pi} \sum_{k=1}^{N}\frac{\sin\left(2 \pi k f_{0}t\right)}{k}$' + '\n' + 'N = 1')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, x_2)

    plt.axis([interval[0], interval[1], -1.5, 1.6])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-1.5, 1.6, 0.5), fontsize=12)

    plt.title('N = 10')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, x_3)

    plt.axis([interval[0], interval[1], -1.5, 1.6])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-1.5, 1.6, 0.5), fontsize=12)

    plt.title('N = 10000')
    plt.grid()

    plt.tight_layout()
    plt.savefig('lab1_3.3.png', bbox_inches='tight', transparent=False)
    plt.show()



def item_04_sum(n, f0, t):
    x = np.zeros(t.shape)

    for k in np.arange(1, n + 1):
        x += np.power(-1,k)*np.sin( 2 * np.pi *(2* k +1)* f0 * t )/np.power((2*k+1),2)

    x *= 8 /np.power( np.pi, 2 )    

    return x

def item_04():
    f0 = 0.25
    interval = [0, 6. / f0]
    t = np.linspace(interval[0], interval[1], 1e04)

    n = 1
    x_1 = item_04_sum(n, f0, t)

    n = 10
    x_2 = item_04_sum(n, f0, t)

    n = 10000
    x_3 = item_04_sum(n, f0, t)

    plt.figure(facecolor='w', figsize=(8, 8))

    # Subplt of 3 lines, 1 column, go to figure 1
    plt.subplot(3, 1, 1)
    plt.plot(t, x_1)

    plt.axis([interval[0], interval[1], -0.1, 0.1])
    plt.xticks(np.arange(interval[0], interval[1]+1), fontsize=12)
    plt.yticks(np.arange(-0.1, 0.11, 0.05), fontsize=12)
    
    plt.title('Lab1-3.4' + '\n' + r'$x(t)=\frac{8}{\pi^{2}}\sum_{k=1}^{N}(-1)^{k}\frac{\sin(2\pi(2k+1)f_{0}t)}{(2k+1)^{2}}$' + '\n' + 'N = 1')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, x_2)

    plt.axis([interval[0], interval[1], -0.2, 0.2])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-0.2, 0.21, 0.05), fontsize=12)

    plt.title('N = 10')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, x_3)

    plt.axis([interval[0], interval[1], -0.2, 0.2])
    plt.xticks(np.arange(interval[0], interval[1] + 1), fontsize=12)
    plt.yticks(np.arange(-0.2, 0.21, 0.05), fontsize=12)

    plt.title('N = 10000')
    plt.grid()

    plt.tight_layout()
    plt.savefig('lab1_3.4.png', bbox_inches='tight', transparent=False)
    plt.show()


if __name__ == '__main__':
    main()
