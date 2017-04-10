#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt


def main():
    item_01()


def item_01():
    ni1=[0,32]
    
    
    n1=np.arange(ni1[0],ni1[1]+1,1)
    x1=np.cos(2*np.pi*n1/16.)
    
    
    
    plt.figure(facecolor='w',figsize=(7,3.5))
    
    plt.stem(n1,x1,'k',linewidth=1.5)
    plt.axis([ni1[0],ni1[1],-1.1,1.1])
    plt.xlabel
    plt.grid()
    
    plt.show()
    
    
    plt.savefig("lab1_4.1.png", bbox_inches='tight', transparent=False)
    
    plt.close('all')


def item_02():
    pass


def item_03():
    pass


def item_04():
    pass


def item_05():
    pass


def item_06():
    pass


if __name__ == '__main__':
    main()
