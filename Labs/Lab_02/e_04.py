# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from SoundPlay import soundPlay
import sys
sys.path.append('../../PySynth')
import pysynth_s as pysynths
import pysynth_e as pysynthe




song=["c5",4],["d5",4]
pysynths.make_wav(song, bpm = 132, fn = "x4.wav")

sampFreq, snd = wavfile.read('x4.wav') # load the data


#converter os pontos para floats entre -1 e 1
x = snd / 2.**13


t = np.arange(0, len(x)) /np.float(sampFreq)

#plot do sinal
plt.figure(facecolor = 'w', figsize = (10, 20))
plt.plot(t[0:1000], x[0:1000], 'k')
plt.xlabel(r'$t$ (segundos)')
plt.ylabel('Intensidade')
plt.savefig("lab2_ex4_Sinal.png", bbox_inches = 'tight', transparent = False)
plt.show()  

plt.figure(facecolor = 'w', figsize = (10, 20))
plt.plot(x)
plt.savefig("lab2_ex4_.png", bbox_inches = 'tight', transparent = False)
plt.show()

N=4096
#plot do espectro do sinal
xfft = np.fft.fft(x[0:N])

freq1 = np.fft.fftfreq(len(xfft)) * sampFreq
x1mag = np.abs(xfft) / N
Xfase = np.angle(xfft)


#Espectro amplitude
plt.figure(facecolor = 'w', figsize = (10, 20))
plt.stem(freq1, x1mag, 'k', linewidth = 3)

plt.ylabel('Espectro amplitude', fontsize = 18)
plt.xlabel('f(Hz)', fontsize = 18)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.grid()
plt.savefig("lab2_ex4_espectroAmplitude.png", bbox_inches='tight', transparent = False)
plt.figure(facecolor = 'w', figsize = (10, 20))
plt.show()

#Espectro Fase
plt.figure(facecolor = 'w', figsize = (10, 20))
plt.stem(freq1, Xfase, 'k', linewidth = 3)
#plt.axis([-1100, 1100, -np.pi, np.pi])
plt.ylabel('Espectro de fase', fontsize = 18)
plt.xlabel('f(Hz)', fontsize=18)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.grid()
plt.savefig("lab2_ex4_espectroFase.png", bbox_inches = 'tight', transparent = False)
plt.show()


#espectrograma
NFFT = 512*4
plt.figure(facecolor = 'w', figsize = (30, 20))
plt.specgram(x, NFFT = NFFT, Fs = sampFreq, noverlap = 0)
plt.savefig("lab2_ex4_espectrograma.png", bbox_inches = 'tight', transparent = False)

