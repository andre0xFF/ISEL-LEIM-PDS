import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt


N=500
n=np.arange(0,N)

x=10.0+2*np.cos(np.pi/3.0*n)+5*np.cos(3*np.pi/4*n)
count=0

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
    global count
    count+=1
    b=count+1

    
    y = ss.firwin(101, wc, pass_zero=pass_zero, window=window)
    w, h = ss.freqz(y,1)
    ypbx=ss.lfilter(y, 1, x)

    plt.figure()
    plt.plot(w, abs(h))
    plt.savefig("2-"+str(count)+"."+str(count)+".png", bbox_inches = 'tight', transparent = False)
    plt.show()
    
    
    
    plt.figure(facecolor='w',figsize=(30,25))
    
    
    plt.subplot(111)
    plt.plot(n,x,'r')
    plt.plot(n,ypbx,lw=4)
    plt.savefig("2-"+str(count)+"."+str(b)+".png", bbox_inches = 'tight', transparent = False)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    
    

def item_d():
    
    y = ss.firwin(101, 1 / 4, pass_zero=False, window ='blackman')
    w, h = ss.freqz(y)
    plt.figure()
    plt.subplot(131)
    plt.title('window = blackman',fontsize = 15)
    plt.plot(w, 20 * np.log(abs(h)))
    plt.show()
    
    plt.subplot(132)
    plt.title('window = hamming',fontsize=15)
    y = ss.firwin(101, 1 / 4, pass_zero=False)
    w, h = ss.freqz(y)
    plt.plot(w, 20 * np.log(abs(h)))
    plt.show()
    
    
    plt.subplot(133)
    plt.title('window = boxcar',fontsize=15)
    y = ss.firwin(101, 1 / 4, pass_zero=False,window = 'boxcar')
    w, h = ss.freqz(y)
    plt.plot(w, 20 * np.log(abs(h)))
    plt.savefig("2-4.png", bbox_inches = 'tight', transparent = False)
    plt.show()
    
    

if __name__ == "__main__":
    main()
