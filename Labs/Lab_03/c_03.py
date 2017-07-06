#Processamento Digital de Sinais - 2016/17
# Reading Accelerometer Data

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg

def findPeakDist(data):

	# 3Hz is fastest -> peaks no closer than 1/3 sec
	# 1/3 sec, @ 20Hz sampling rate -> 6-7 samples is closest

	# distance between peaks
	N = 8; # num of terms to look at on either side of value

#	hMin = 0.75
	hMin = 2.0

	# Iter through looking for min, max pair
	priorPeak = False

	stepCount = 0

	for i in xrange(N, len(data) - N):
		if ((max(data[i:i+N]) - min(data[i-N:i])) > hMin):
			if (not priorPeak):
				print i
				stepCount += 1
			priorPeak = True
		else:
			priorPeak = False

	print "STEPS FOUND: ", stepCount


#loading accelerometer data
#data=np.loadtxt("walk_example.txt")
#data=np.loadtxt("default__1.txt")
#data=np.loadtxt("WALK_30_30.txt")
#data=np.loadtxt("WALK_10.txt")
data=np.loadtxt("climb_11.txt")
#data=np.loadtxt("stairs_example.txt")
#data is a np.array with 4 columns 
# X Y Z time_from_previous_sample(ms)

#histogram of sampling period
plt.close('all')
plt.figure(facecolor='w',figsize=(25,18))
plt.title('Histogram of sampling period [ms]')
plt.hist(data[:,3])

#converting to time-stamps
t=np.cumsum(data[:,3])
#acc=np.hstack((t.reshape(len(t),1),data[:,:3]))
acc=data[:,:3]

#plotting data
plt.figure(facecolor='w',figsize=(25,18))
plt.title('Accelerometer Data')
plt.plot(t,acc[:,0],t,acc[:,1],t,acc[:,2])
plt.legend(['X','Y','Z'])
plt.xlabel('t[ms]')
plt.ylabel('[m/s^2]')

x=data[:,0]
y=data[:,1]
z=data[:,2]

modulo=np.sqrt(x**2+y**2+z**2)
n=np.arange(np.size(modulo))

plt.figure(facecolor='w',figsize=(25,15))
plt.plot(n,modulo,'k',linewidth=2)

lf=24
b = (1./lf)*np.ones(lf)
a=[1.]
y=sg.lfilter(b,a,modulo)

plt.plot(n,y,'r',linewidth=3)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

plt.figure(facecolor='w',figsize=(25,15))

#y1=y[280:2100]
#t1=t[280:2100]
#y1=y[890:1600]
#t1=t[890:1600]
y1=y[600:2000]
t1=t[600:2000]
plt.plot(t1,y1,'r',linewidth=3)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
#derivada=sg.lfilter([1,-1],[1],modulo)
#plt.plot(derivada,'r')
#
#derivada2=sg.lfilter([1,-1],[1],derivada)
#plt.plot(derivada2,'b')


findPeakDist(y1)
