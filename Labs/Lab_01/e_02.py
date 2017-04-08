#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add graph titles, latex formulas, axis subtitles, axis best intervals


def main():
    item_01()


def item_01():
    interval = [-4.5, -1.5]
    t = np.linspace(interval[0], interval[1], 1e04)
    x = np.zeros(len(t))

    #procura os indices dos t que verificam ambas as condições e nesses sitios o x vai valer 1
    x[(-2 * t - 4 >= 0) & (-t - 4 <= 0)] = 1

    plt.close()
    plt.figure(facecolor='w', figsize=(7, 5))
    plt.plot(t, x, 'k', linewidth=1.5)
    plt.axis([interval[0], interval[1], -0.1, 1.1])
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlabel('t(s)',fontsize=10)
    plt.ylabel('x(t)',fontsize=10)
    plt.text(-3.5,1.2,'Lab-1 1.5',fontsize=24)
    plt.title(r'$x(t)=u(-2t-4)-u(-t-4)')
    plt.grid()
    
    plt.savefig("lab2_1.1.png",bbox_inches='tight',transparent=False)
    plt.show()
    # plt.savefig()


def item_02():
    # t1=[-2.1,-1.4]
    # figFile('dsadsa')
    #
    # t=np.linspace(t1[0],t1[1],1e4)
    # x=np.zeros(t.shape)
    # u1=(t+2. >= 0) * 1.
    # u2=(t+1.53 >= 0) * 1.
    # x = np.cos(30. * np.pi * t) * (u1 - u2)
    #
    # plt.close('all')
    # plt.figure(facecolor='w', figsize=(7,5))
    # plt.plot(t, x, 'k', linewidth=1.5)
    # plt.axis([t1[0], t1[1], -1.1, 1.1])
    # plt.label()
    pass

def item_03():
    # t1=[-1, 5]
    # t=np.linspace(t1[0], t1[1], 1e4)
    # x=np.zeros(t.shape)
    # u1=(t >= 0.) * 1.
    # u2=(t-1 >= 0.) * 1.
    pass


if __name__ == '__main__':
    main()
