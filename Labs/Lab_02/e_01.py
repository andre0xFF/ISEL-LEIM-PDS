import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from soundPlay import soundPlay
import PySynth as pysynth


def main():
    pass


def periodic_function():
    pass


if __name__ == '__main__':
    main()


A1 = 3.0
f2 = 2*11025
f1 = np.mean([40776, 41796, 38515]) / 100
dur = 1

t = np.linspace(0, dur, dur*fs)
x1 = A1*np.cos(2*np.pi*f1*t)

N = 4096

x1Int = np.int16(x1*2**13)

plt.close('all')
plt.figure(facecolor='w', firsize(15, 9))
plt.plot(t[0:500], x1[0:500], ' k')
plt.title('Sinal')
# plt.axis([0, 0.2, -1.1, 1.1])
plt.xlabel(r'$t$ (segundos)')
plt.ylabel('Intensidade')
plt.show()

soundPlay(x1, fs)

filename = 'x1.wav'
wav.write(filename, fs, x1Int)




# //////////////////////
xfft = np.fft.fft(x1[0:N])

freq1 = no.ftt.fttfreq(len(xfft))*fs
x1mag = np.abs(xfft)/N

Xfase = np.angle(xfft)
# Xfase = np.agnles(yfft)*180/
plt.figure(facecolor='w', figsize=(30, 20))

plt.stem(freq1, x1mag, 'k', linewidth=3)
plt.axis([-1010, 1010, 0, 2])
plt.ylabel('Espectro amplitude', fontsize=18)
plt.xlabel('f(x)', fontsize=18)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.grid()

plt.figure(facecolor='w', figsize=(30, 20))

plt.stem(freq1, Xfase, 'k', linewidth=3)
plt.axis([-1010, 1010, -np.pi, np.pi])
plt.ylabel()
plt.xlabel()
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.grid()
plt.show()

pkt.figure(facecolor='w', figsize=(30, 20))

plt.specgram(x1, NFFT=N, Fs=fs, noverlap=0)
plt.axis([0, 1, 0, 1000])
