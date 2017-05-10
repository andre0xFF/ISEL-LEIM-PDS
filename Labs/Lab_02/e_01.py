#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from soundPlay import soundPlay
import sys
sys.path.append('../../PySynth')
import pysynth_s as pysynth


def sinwave(A, f):
    pass


def main():
    pass


def periodic_function():
    pass


if __name__ == '__main__':
    main()


A1 = 3.0
f2 = 2 * 11025
f1 = np.mean([40776, 41796, 38515]) / 100

# Podemos ter a duracao que quisermos
dur = 1

t = np.linspace(0, dur, dur * fs)
x1 = A1 * np.cos(2 * np.pi * f1 * t)

N = 4096

# Multiplicar por um numero grande para aumentar o numero "empurrar a virgula"
x1Int = np.int16(x1 * 2**13)

plt.close('all')
plt.figure(facecolor='w', figsize(15, 9))
plt.plot(t[0:500], x1[0:500], 'k')
plt.title('Sinal')
plt.axis('tight')
# plt.axis([0, 0.2, -1.1, 1.1])
plt.xlabel(r'$t$ (segundos)')
plt.ylabel('Intensidade')
plt.show()

# Ouvir o som. Nao e' obrigatorio
soundPlay(x1, fs)

filename = 'x1.wav'
wav.write(filename, fs, x1Int)


# //////////////////////
# b) fazer os calculos analiticos a' mao
# explicar no relatorio como se interpreta o espectograma..

xfft = np.fft.fft(x1[0:N])

freq1 = no.ftt.fttfreq(len(xfft)) * fs
x1mag = np.abs(xfft) / N

Xfase = np.angle(xfft)
# Xfase = np.agnles(yfft)*180/np.pi
plt.figure(facecolor='w', figsize=(30, 20))
# plt.subplot(312)
plt.stem(freq1, x1mag, 'k', linewidth=3)
plt.axis([-1010, 1010, 0, 2])
plt.ylabel('Espectro amplitude', fontsize=18)
plt.xlabel('f(Hz)', fontsize=18)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.grid()

plt.figure(facecolor='w', figsize=(30, 20))
# plt.subplot(313)
# Xfase = np.angle(X_fft)*180/np.pi
plt.stem(freq1, Xfase, 'k', linewidth=3)
plt.axis([-1010, 1010, -np.pi, np.pi])

plt.ylabel('Espectro de fase', fontsize=18)
plt.xlabel('f(Hz)', fontsize=18)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.grid()
plt.show()

plt.figure(facecolor='w', figsize=(30, 20))

plt.specgram(x1, NFFT=N, Fs=fs, noverlap=0)
plt.axis([0, 1, 0, 1000])
