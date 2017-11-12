# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:53:53 2017

"""

import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt


N=500
n=np.arange(0,N)

x=10+2*np.cos(np.pi/3*n)+5*np.cos(3*np.pi/4*n)

def main():
     item_a()
     item_c()


def item_a():
    # c = 1

    w, h = ss.freqz([1], [1, 0.8])
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.title('b = 1; r = 0.8',fontsize=15)
    plt.savefig("1-a.1.png", bbox_inches = 'tight', transparent = False)
    plt.show()
    
    

    w, h = ss.freqz([1], [1, 0.9])
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.title('b = 1; r = 0.9',fontsize=15)
    plt.savefig("1-a.2.png", bbox_inches = 'tight', transparent = False)
    plt.show()

    w, h = ss.freqz([1], [1, 0.1])
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.title('b = 1; r = 0.1',fontsize=15)
    plt.savefig("1-a.3.png", bbox_inches = 'tight', transparent = False)
    plt.show()

    # c = 2
    w, h = ss.freqz([1], [1, 0, 0.8])
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.title('b = 1; r = 0.8',fontsize=15)
    plt.savefig("1-a.4.png", bbox_inches = 'tight', transparent = False)
    plt.show()

    w, h = ss.freqz([1], [1, 0, 0.9])
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.title('b = 1; r = 0.9',fontsize=15)
    plt.savefig("1-a.5.png", bbox_inches = 'tight', transparent = False)
    plt.show()

    w, h = ss.freqz([1], [1, 0, 0.1])
    plt.figure()
    plt.plot(w, np.abs(h))
    plt.title('b = 1; r = 0.1',fontsize=15)
    plt.savefig("1-a.6.png", bbox_inches = 'tight', transparent = False)
    plt.show()

#    return d

def item_c():
    # c = 1

    plt.figure(facecolor='w',figsize=(30,25))
    plt.subplot(221)
    
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title(r'$x= 10 + 2* \cos\left(\frac{\pi}{3n}\right)+5*\cos\left(\frac{3\pi}{4n}\right)$',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('x',fontsize=15)
    plt.grid()
    plt.show()
    
    y = system(1, 1, 0.8, x)
    
    plt.subplot(222)
    plt.plot(n,y,'k',lw=3)
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('b = 1; r = 0.8',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('y',fontsize=15)
    plt.grid()
    
    plt.show()
    
    
    y = system(1, 1, 0.9, x)
    
    plt.subplot(223)
    plt.plot(n,y,'k',lw=3)
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('b = 1; r = 0.9',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('y',fontsize=15)
    plt.grid()

    plt.show()
    
    y = system(1, 1, 0.1, x)
    
    plt.subplot(224)
    plt.plot(n,y,'k',lw=3)
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('b = 1; r = 0.1',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('y',fontsize=15)
    plt.grid()
    plt.savefig("1-c.1.png", bbox_inches = 'tight', transparent = False)
    plt.show()
    
    
    
     # c = 2

    plt.figure(facecolor='w',figsize=(30,25))
    plt.subplot(221)
    
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title(r'$x= 10 + 2* \cos\left( \frac{\pi}{3n} \right)+5*\cos \left( \frac{3\pi}{4n}\right)$',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('x',fontsize=15)
    plt.grid()
    
    plt.show()
    
    
    y = system(2, 1, 0.8, x)
    
    plt.subplot(222)
    plt.plot(n,y,'k',lw=3)
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('b = 1; r = 0.8',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('y',fontsize=15)
    plt.grid()
    
    plt.show()
    
    
    y = system(2, 1, 0.9, x)
    
    
    plt.subplot(223)
    plt.plot(n,y,'k',lw=3)
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('b = 1; r = 0.9',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('y',fontsize=15)
    plt.grid()

    plt.show()
    
    
    
    y = system(2, 1, 0.1, x)
    
    
    plt.subplot(224)
    plt.plot(n,y,'k',lw=3)
    plt.plot(n,x,'r')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('b = 1; r = 0.1',fontsize=15)
    plt.xlabel('n',fontsize=15)
    plt.ylabel('y',fontsize=15)
    plt.grid()
    plt.savefig("1-c.2.png", bbox_inches = 'tight', transparent = False)
    plt.show()
    


def system(c, b, r, x):
    if c == 1:
        
        b1 = np.array([1])
        a1 = np.zeros([b + 1])
        a1[0] = 1
        a1[-1] = r
    
        return ss.lfilter(b1, a1, x)
    if c == 2:
        
        return ss.lfilter([1], [1,0,r], x)

if __name__ == "__main__":
    main()
