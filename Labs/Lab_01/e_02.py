#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add graph titles, latex formulas, axis subtitles, axis best intervals


def main():
    item_01()
    item_02()
    


def item_01():
    interval = [-4.5, -1.5]
    
    t = np.linspace(interval[0], interval[1], 1e04)
    
    x = np.zeros(len(t))

    #procura os indices dos t que verificam ambas as condições e nesses sitios o x vai valer 1
    x[(-2 * t - 4 >= 0) & (-t - 4 <= 0)] = 1

    plt.close()
    plt.figure(facecolor='w')
    plt.plot(t, x, 'k', linewidth=1.5)
    
    plt.axis([interval[0], interval[1], -0.1, 1.1])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.xlabel('t(s)',fontsize=12)
    plt.ylabel('x(t)',fontsize=12)
    
    
    plt.title('Lab-1- 2.1'+'\n'+ r'$x(t)=u(-2t-4)-u(-t-4)$')
    plt.grid()
    
    plt.savefig("lab2_1.1.png",bbox_inches='tight',transparent=False)
    plt.show()


def item_02():
     interval=[-2.1,-1.4]
   
     t=np.linspace(interval[0],interval[1],1e4)
     x=np.zeros(t.shape)
     
     u1=(t+2 >= 0) 
     u2=(t+1.53 >= 0)
    
     
     x = np.cos(2 * np.pi * 15 * t) * (u1 - u2)
    
     plt.close('all')
     plt.figure(facecolor='w')
     plt.plot(t, x, 'k', linewidth=1.5)
  
     plt.xticks(fontsize=12)
     plt.yticks(fontsize=12)
     
     plt.xlabel('t(s)',fontsize=12)
     plt.ylabel('x(t)',fontsize=12)
     
     plt.title('Lab-1- 2.2'+'\n'+ r'$x(t)=cos(2 \pi(15)t) (u(t+2)-u(t+1.53))$')
     plt.grid()
     
     plt.savefig("lab1_2.2.png",bbox_inches='tight',transparent=False)
     plt.show()
    

def item_03():
    # t1=[-1, 5]
    # t=np.linspace(t1[0], t1[1], 1e4)
    # x=np.zeros(t.shape)
    # u1=(t >= 0.) * 1.
    # u2=(t-1 >= 0.) * 1.
    


if __name__ == '__main__':
    main()
