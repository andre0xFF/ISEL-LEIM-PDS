import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg

def encontDistPic(data):

	

	# distancia entre picos
	N = 8

	hMin = 0.8


	# Iteração para encontrar par min e max
	picoAnt = False

	stepCount = 0

	for i in range(N, len(data) - N):
		if ((max(data[i:i+N]) - min(data[i-N:i])) > hMin):
			if (not picoAnt):
				stepCount += 1
			picoAnt = True
		else:
			picoAnt = False

	print ("passos: ", stepCount)



data=np.loadtxt("WALK_10.txt")


#histograma do periodo de amostras

plt.close('all')
plt.figure(facecolor='w',figsize=(30,20))
plt.title('Histograma do periodo de amostras[ms]')
plt.hist(data[:,3])
plt.savefig("histograma.png", bbox_inches = 'tight', transparent = False)

t=np.cumsum(data[:,3])

acc=data[:,:3]

#plotting data
plt.figure(facecolor='w',figsize=(25,18))
plt.title('data do acelerometro')
plt.plot(t,acc[:,0],t,acc[:,1],t,acc[:,2])
plt.savefig("data acelerometro.png", bbox_inches = 'tight', transparent = False)
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
plt.savefig("data e filtro.png", bbox_inches = 'tight', transparent = False)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

plt.figure(facecolor='w',figsize=(25,15))


y1=y[600:2000]
t1=t[600:2000]
plt.plot(t1,y1,'r',linewidth=3)
plt.savefig("data após filtro.png", bbox_inches = 'tight', transparent = False)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)



encontDistPic(y1)
