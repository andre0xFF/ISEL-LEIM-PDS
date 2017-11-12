#Processamento Digital de Sinais - 2016/17
# Reading Accelerometer Data

import numpy as np
import matplotlib.pyplot as plt

#loading accelerometer data
data=np.loadtxt("stairs_example.txt")
#data=np.loadtxt("stairs_example.txt")
#data is a np.array with 4 columns 
# X Y Z time_from_previous_sample(ms)

#histogram of sampling period
plt.figure()
plt.title('Histogram of sampling period [ms]')
plt.hist(data[:,3])

#converting to time-stamps
t=np.cumsum(data[:,3])

#acc=np.hstack((t.reshape(len(t),1),data[:,:3]))
acc=data[:,:3]

#plotting data
plt.figure()
plt.title('Accelerometer Data')
plt.plot(t,acc[:,0],t,acc[:,1],t,acc[:,2])
plt.legend(['X','Y','Z'])
plt.xlabel('t[ms]')
plt.ylabel('[m/s^2]')
plt.show()