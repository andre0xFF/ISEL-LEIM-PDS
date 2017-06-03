# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:46:19 2017

@author: Danie
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from SoundPlay import soundPlay
import sys
sys.path.append('../../PySynth')
import pysynth_s as pysynth


FS=11025
NFFT=512*2

dur=2.
plt.close("all")


Song=["C",4],["D",4],["E",4],["F",4]

noteList6=[]
notedur6=[]
xMusica=[]
#NotasDic={'c3':131,}
NotasDic={'C':16,'D':18,'E':21,'F':22,'G':25,'A':28,'B':31,'C*':17,'D*':19,'F*':23,'G*':26,'A*':29,
          'C1':33,'D1':37,'E1':41,'F1':44,'G1':49,'A1':55,'B1':62,'C1*':35,'D1*':39,'F1*':46,'G1*':52,'A1*':58}

print(NotasDic['C'])
for i, x in enumerate(Song):
    noteList6=np.hstack((noteList6,x[0]))
    notedur6=np.hstack((notedur6,dur/x[1]))
    

def Music(notelist,notaDur):
    
    
    intDur=0.05
    wavType=1
    FS=11025
    
    x=np.array([])
    
    for i in range(0,len(notelist)):
        xtmp=Note_tone(notelist[i],notaDur[i],intDur,wavType,FS)
        
        
        x=np.hstack((x,xtmp))
    return (x)

def ADSR_env1(N=[]):
    Dur = (0.1, 0.2, 0.6, 0.1)
    nA = np.floor(N * Dur[0])
    nD = np.floor(N * Dur[1])
    nS = np.floor(N * Dur[2])
    nR = N - nA - nD - nS

    # faltam aqui coisas
    #linha(recta) que vai de 0 a 1 com nA pontos
    xA = np.linspace(0,1,nA)
    xD = np.linspace(1, .8, nD)
    xS = np.ones(nS) * 0.8
    xR = np.linspace(0.8, 0, nR)
    # faltam aqui coisas
    
    #xEnv=np.hstack(xA,x[0])
    #xEn0 = np.hstack(xA,xD,xS,xR)
    
#    xEnv=np.hstack(xA,xD,xS,xR)
    
    
    return xEnv
    
def Note_tone(nota=[], notaDur=[], intDur=[], wavType=[], Fs=[]):

    print(nota+" "+ (str)(NotasDic[nota]))
  
    fc=NotasDic[nota]*50

    t = np.arange(0, notaDur, 1 / Fs)

    if wavType == 1:
        print("wave type 1")
        x = np.cos(2 * np.pi * fc * t)
        
    elif wavType == 2:
        x = np.square(2 * np.pi * fc * t)
    elif wavType == 3:
        x = np.sawtooth(2 * np.pi * fc * t, 0.5)
    elif wavType== 4:
        x = np.sawtooth(2 * np.pi * fc * t)
    else:
        print ('\n wave type (%d) not available (only ints 1-4)\n'%wavType)
    
    
    plt.plot(t[0:1000], x[0:1000], 'k')
    plt.title('Sinal Nota -'+nota)
    plt.xlabel(r'$t$ (segundos)')
    plt.ylabel('Intensidade')
    plt.show()
#    xEnv = ADSR_env1(len(x))
#    return xEnv
    return x

#    xMusica=np.hstack(xMusica,x[0])
#  #  xEnv = ADSR_env1(len(x))
#    plt.figure(facecolor='w')
#    #plt.plot(xEnv)
#    soundPlay.soundPlay(x,FS)
#   # soundPlay.soundPlay(xEnv,FS)
#    plt.title('Sinal Nota -'+nota)
#    plt.xlabel(r'$t$ (segundos)')
#    plt.ylabel('Intensidade')
#    plt.show()
#    plt.plot(t[0:1000], x[0:1000], 'k')
#    
#    N=512
#    fs=22050*2
#    xfft = np.fft.fft(x[0:N])
#
##freq1=np.fft.fftfreq(len(xfft))*fs
#    freq1 = np.fft.fftfreq(len(xfft)) * fs
#    x1mag = np.abs(xfft) / N
#
#   # Xfase = np.angle(xfft)
## Xfase = np.agnles(yfft)*180/np.pi
#    
#    plt.figure(facecolor='w', figsize=(10, 20))
#    plt.stem(freq1, x1mag, 'k', linewidth=3)




N=4096
x=Music(noteList6,notedur6)
soundPlay.soundPlay(x,FS)
filename = 'x2.wav'
x1Int = np.int16(x * 2**13)
wavfile.write(filename, FS, x1Int)

xfft = np.fft.fft(x[0:N])

freq1 = np.fft.fftfreq(len(xfft)) * FS
x1mag = np.abs(xfft) / N
Xfase = np.angle(xfft)

plt.figure(facecolor='w', figsize=(10, 20))

#Espectro amplitude
plt.stem(freq1, x1mag, 'k', linewidth=3)


plt.ylabel('Espectro amplitude', fontsize=18)
plt.xlabel('f(Hz)', fontsize=18)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.grid()
plt.savefig("lab2ex1_espectrograma.png", bbox_inches='tight', transparent=False)
plt.figure(facecolor='w', figsize=(10, 20))

#Espectro Fase
Xfase = np.angle(xfft)
plt.stem(freq1, Xfase, 'k', linewidth=3)
plt.axis([-1100, 1100, -np.pi, np.pi])

plt.ylabel('Espectro de fase', fontsize=18)
plt.xlabel('f(Hz)', fontsize=18)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.grid()
plt.show()

#Espectrograma

plt.figure(facecolor='w', figsize=(30, 20))
#plt.specgram(x, NFFT=N*2, Fs=FS*2, noverlap=0)
plt.specgram(x, NFFT=N, Fs=FS, noverlap=0)

#plt.axis([0, 1, 0, FS])



#np.fft.fftfreq

