#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add graph titles, latex formulas, axis subtitles, axis best intervals


def main():
    item_01()
    item_02()
    item_03()
    item_04()
    item_05()

def item_01():
    #array that contains "area" of the graphic we want to plot
    interval = [44,50]

    #Creates an array of evenly spaced numbers in designated range
    t = np.linspace(interval[0], interval[1], 1e04)
    
    #wave function
    x = 2 * np.cos(20 * np.pi * t + np.pi / 3) + np.sin(22 * np.pi * t - np.pi / 4)
    
    #closes previous plots
    plt.close('all')
    
    #creates figure of the graphic with the determined size and color
    plt.figure(facecolor='y',figsize=(12,8))
    
    #draws graphic
    draw_graph(t,x)
    
    #selects the axis to be displayed in the graphic
    plt.axis([interval[0]-0.5,interval[1]+0.5,-3.5,3.5])
    
    #determines the ticks axis range and size
    plt.xticks(np.arange(interval[0],interval[1]+1),fontsize=15)
    plt.yticks(np.arange(-3.5,3.6),fontsize=15)
    
    #Formats the graphic with axis names, text labels, and with various informations of the wave being analyzed
    plt.xlabel('t(s)',fontsize=20)
    plt.ylabel('x(t)',fontsize=20)   
    plt.text(46.5,3.50,'Lab-1 1.1',fontsize=24) 
    plt.text(46,3.15,r'$x(t)=2\cos \left(20 \pi t + \frac{\pi}{3} \right) +  \sin \left(22\pi t- \frac{\pi}{4}\right)$',fontsize=15)
    
    #Enables the graphic grid display
    plt.grid()
    
    #Saves graphic image
    plt.savefig("lab1_1.1.png",bbox_inches='tight',transparent=False)
    
    #displays created Graphic
    plt.show()
    

def item_02():
    #array that contains "area" of the graphic we want to plot
    interval = [121, 123]
    
    #Creates an array of evenly spaced numbers in designated range
    t = np.linspace(interval[0], interval[1], 1e03)
    
     #wave function
    x = np.cos(540 * np.pi * t + np.pi / 2) + np.cos(545 * np.pi * t + np.pi / 2)
    
    #closes previous plots
    plt.close('all')
    
    #creates figure of the graphic with the determined size and color
    plt.figure(facecolor='y',figsize=(12,8))
    
    #draws graphic
    draw_graph(t,x,"m")
    
    #selects the axis to be displayed in the graphic
    plt.axis([interval[0]-0.2,interval[1]+0.2,-3,3])
    
    #determines the ticks axis range and size
    plt.xticks(np.arange(interval[0],interval[1]+1),fontsize=15)
    plt.yticks(np.arange(-3,4),fontsize=15)
    
    #Formats the graphic with axis names, text labels, and with various informations of the wave being analyzed
    plt.xlabel('t(s)',fontsize=20)
    plt.ylabel('x(t)',fontsize=20)
    plt.text(121.7,3.50,'Lab-1 1.2',fontsize=24)
    plt.text(121.5,3.15,r'$x(t)=\cos \left(540 \pi t + \frac{\pi}{2} \right) +  \cos \left(545\pi t- \frac{\pi}{2}\right)$',fontsize=15)
    
    #Enables the graphic grid display
    plt.grid()
    
    #Saves graphic image
    plt.savefig("lab1_1.2.png",bbox_inches='tight',transparent=False)

    #displays created Graphic
    plt.show()


def item_03():
    #array that contains "area" of the graphic we want to plot
    interval = [31, 33]
    
    #Creates an array of evenly spaced numbers in designated range
    t = np.linspace(interval[0], interval[1], 1e04)
    
    #wave function
    x = (1 / 3 + 2 / 3 * np.cos(5 * np.pi * t)) * np.cos(100 * np.pi * t)
    
    #closes previous plots
    plt.close('all')
    
    #creates figure of the graphic with the determined size and color
    plt.figure(facecolor='y',figsize=(12,8))
    
    #draws graphic
    draw_graph(t,x,"r")
    
    #selects the axis to be displayed in the graphic
    plt.axis([interval[0]-0.2,interval[1]+0.2,-3,3])
    
    #determines the ticks axis range and size
    plt.xticks(np.arange(interval[0],interval[1]+1),fontsize=15)
    plt.yticks(np.arange(-3,3),fontsize=15)
    
    #Formats the graphic with axis names, text labels, and with various informations of the wave being analyzed
    plt.xlabel('t(s)',fontsize=20)
    plt.ylabel('x(t)',fontsize=20)
    plt.text(31.7,3.50,'Lab-1 1.3',fontsize=24)
    plt.text(31.5,3.15,r'$x(t)=\left(\frac{1}{3} +\frac{2}{3}\cos \left(5 \pi t \right)\right) \times  \cos \left(100\pi t\right)$',fontsize=15)
    
    #Enables the graphic grid display
    plt.grid()
    
    #Saves graphic image
    plt.savefig("lab1_1.3.png",bbox_inches='tight',transparent=False)
    
    #displays created Graphic
    plt.show()

def item_04():
    #array that contains "area" of the graphic we want to plot
    interval = [11.2, 11.3]

    #Creates an array of evenly spaced numbers in designated range
    t = np.linspace(interval[0], interval[1], 1e04)
    
    #wave function
    x = np.cos(2 * np.pi *t* (440 + np.cos(20 * np.pi * t)))
    
     #closes previous plots
    plt.close('all')
    
    #creates figure of the graphic with the determined size and color
    plt.figure(facecolor='y',figsize=(12,8))

    #draws graphic
    draw_graph(t, x)

    #selects the axis to be displayed in the graphic
    plt.axis([interval[0]-0.005,interval[1]+0.005,-2,2])
    
    #Formats the graphic with axis names, text labels, and with various informations of the wave being analyzed
    plt.xlabel('t(s)',fontsize=20)
    plt.ylabel('x(t)',fontsize=20)
    plt.text(11.235,3.50,'Lab-1 1.4',fontsize=24)
    plt.text(11.23,3.15,r'$x(t)=\cos \left(2 \pi t  \left( 440 + \cos \left(20 \pi t \right) \right) \right)$',fontsize=15)
    
    #Enables the graphic grid display
    plt.grid()
    
    #Saves graphic image
    plt.savefig("lab1_1.4.png",bbox_inches='tight',transparent=False)
    
    #displays created Graphic
    plt.show()


def item_05():
    #array that contains "area" of the graphic we want to plot
    interval = [-4, 4]

    #Creates an array of evenly spaced numbers in designated range
    t = np.linspace(interval[0], interval[1], 1e04)
    
    #wave function
    #x = np.sinc(3 * np.pi * t)
    #x=np.sin(3*np.pi*t)/(3*np.pi*t)
    x= np.sinc(3*t)
    
    #closes previous plots
    plt.close('all')
    
    #creates figure of the graphic with the determined size and color
    plt.figure(facecolor='y',figsize=(12,4))

    #draws graphic
    draw_graph(t, x)
    
    #selects the axis to be displayed in the graphic
    plt.axis([interval[0]-0.5,interval[1]+0.5,-0.4,1.1])
    
    #Formats the graphic with axis names, text labels, and with various informations of the wave being analyzed
    plt.xlabel('t(s)',fontsize=20)
    plt.ylabel('x(t)',fontsize=20)
    plt.text(-0.5,1.50,'Lab-1 1.5',fontsize=24)
    plt.text(-0.5,3.,r'$x(t)=\frac{\sin\left(3 \pi t\right)}{3 \pi t}$',fontsize=15)
    
    #Enables the graphic grid display
    plt.grid()
    
    #Saves graphic image
    plt.savefig("lab1_1.5.png",bbox_inches='tight',transparent=False)
    
    #displays created Graphic
    plt.show()

def draw_graph(t, x, color=None, lineWidth=None):
    if color is None and lineWidth is None:
        plt.plot(t,x)
    elif color is None and lineWidth is not None:
        plt.plot(t,x,linewidth=lineWidth)
    elif color is not None and lineWidth is None:
        plt.plot(t,x,color)
    else:
        plt.plot(t,x,color,linewidth=lineWidth)


if __name__ == '__main__':
    main()
