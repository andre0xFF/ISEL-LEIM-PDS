# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 20:05:31 2017

@author: isabel surface
"""

# -*- coding: latin-1 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg

####################################################
c=1
r=0.9
a11=[1,r]
b11=[1]
w,H11=sg.freqz(b11,a11)

plt.close('all')
plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(H11),lw=4)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('a=[1,0.9], b=1',fontsize=40)
plt.xlabel('w',fontsize=30)
plt.ylabel('H11',fontsize=30)
plt.grid()
#plt.axis([0,np.pi,0,10])


####################################################
c=1
r=0.8
a12=[1,r]
b12=[1]
w,H12=sg.freqz(b12,a12)

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(H12),lw=4)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('a=[1,0.8], b=1',fontsize=40)
plt.xlabel('w',fontsize=30)
plt.ylabel('H12',fontsize=30)
plt.grid()
#plt.axis([0,np.pi,0,10])


####################################################
c=1
r=0.1
a13=[1,r]
b13=[1]
w,H13=sg.freqz(b13,a13)

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(H13),lw=4)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('a=[1,0.1], b=1',fontsize=40)
plt.xlabel('w',fontsize=30)
plt.ylabel('H13',fontsize=30)
plt.grid()
#plt.axis([0,np.pi,0,10])


####################################################
c=2
r=0.9
a21=[1,0,r]
b21=[1]
w,H21=sg.freqz(b21,a21)

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(H21),'k',lw=4)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('a=[1,0,0.9], b=1',fontsize=40)
plt.xlabel('w',fontsize=30)
plt.ylabel('H21',fontsize=30)
plt.grid()
#plt.axis([0,np.pi,0,10])


####################################################
c=2
r=0.8
a22=[1,0,r]
b22=[1]
w,H22=sg.freqz(b22,a22)

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(H22),'k',lw=4)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('a=[1,0,0.8], b=1',fontsize=40)
plt.xlabel('w',fontsize=30)
plt.ylabel('H22',fontsize=30)
plt.grid()
#plt.axis([0,np.pi,0,10])


####################################################
c=2
r=0.1
a23=[1,0,r]
b23=[1]
w,H23=sg.freqz(b23,a23)

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(H23),'k',lw=4)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('a=[1,0,0.1], b=1',fontsize=40)
plt.xlabel('w',fontsize=30)
plt.ylabel('H23',fontsize=30)
plt.grid()
#plt.axis([0,np.pi,0,10])


####################################################


N=500
n=np.arange(0,N)
#x=10.0+2*np.cos(np.pi/6.0*n)+10*np.cos(np.pi/3*n)
x=10.0+2*np.cos(np.pi/3.0*n)+5*np.cos(3*np.pi/4*n)

y11=sg.lfilter(b11,a11,x)
y12=sg.lfilter(b12,a12,x)
y13=sg.lfilter(b13,a13,x)
y21=sg.lfilter(b21,a21,x)
y22=sg.lfilter(b22,a22,x)
y23=sg.lfilter(b23,a23,x)


plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(221)
plt.plot(n,x)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('x',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('x',fontsize=30)
plt.grid()

plt.subplot(222)
plt.plot(n,y11,lw=4)
plt.plot(n,x,'r')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('y11',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('y11',fontsize=30)
plt.grid()

plt.subplot(223)
plt.plot(n,y12,lw=4)
plt.plot(n,x,'r')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('y12',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('y12',fontsize=30)
plt.grid()

plt.subplot(224)
plt.plot(n,y13,lw=4)
plt.plot(n,x,'r')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('y13',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('y13',fontsize=30)
plt.grid()


plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(221)
plt.plot(n,x)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('x',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('x',fontsize=30)
plt.grid()

plt.subplot(222)
plt.plot(n,y21,lw=4)
plt.plot(n,x,'r')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('y21',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('y21',fontsize=30)
plt.grid()

plt.subplot(223)
plt.plot(n,y22,lw=4)
plt.plot(n,x,'r')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('y22',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('y22',fontsize=30)
plt.grid()

plt.subplot(224)
plt.plot(n,y23,lw=4)
plt.plot(n,x,'r')
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.title('y23',fontsize=40)
plt.xlabel('n',fontsize=30)
plt.ylabel('y23',fontsize=30)
plt.grid()

#############################################
#N=500
#n=np.arange(0,N)
#x=10.0+2*np.cos(np.pi/6.0*n)+10*np.cos(np.pi/3*n)

plt.close('all')
# 
pbx=sg.firwin(101,1/3.,pass_zero=True) # Coef do FIR
 
w,Hpbx=sg.freqz(pbx,1)  # Resposta em freq do FIR
ypbx=sg.lfilter(pbx,1,x)  #Saida do FIR quando a entrada esta x
#
plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(Hpbx))
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
#plt.axis([0,np.pi,0,10])

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(n,x,'r')
plt.plot(n,ypbx,lw=4)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
#plt.axis([0,np.pi,0,10])


# 
pa=sg.firwin(101,1/3.,pass_zero=False)

w,Hpa=sg.freqz(pa,1)
ypa=sg.lfilter(pa,1,x)
#
plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(Hpa))
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
#plt.axis([0,np.pi,0,10])

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(n,x,'r')
plt.plot(n,ypa,lw=4)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
#plt.axis([0,np.pi,0,10])

# 
pb=sg.firwin(101,[1/4.,1/3.],pass_zero=False)
#pb=sg.firwin(101,[1/4.,1/3.],pass_zero=True)
#pb=sg.firwin(101,[1/7.,1/2.],pass_zero=True)

w,Hpb=sg.freqz(pb,1)
ypb=sg.lfilter(pb,1,x)
##
plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(w,np.abs(Hpb))
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
#plt.axis([0,np.pi,0,10])

plt.figure(facecolor='w',figsize=(25,18))

plt.subplot(111)
plt.plot(n,x,'r')
plt.plot(n,ypb,lw=4)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
#plt.axis([0,np.pi,0,10])
