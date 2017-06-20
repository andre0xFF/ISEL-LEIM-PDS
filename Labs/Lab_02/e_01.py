#!/usr/bin/env python3
import sys
sys.path.append('../../PySynth')
sys.path.append('../../soundPlay')

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from SoundPlay import soundPlay

f1 = np.mean([40776 , 41796 , 38515]) / 100
A1 = 3.0
# Podemos ter a duracao que quisermos
dur = 1
fs = 2 * 11025
t = np.linspace(0, dur, dur * fs)

def sinwave(A , f):
    
    return A * np.cos(2 * np.pi * f * t)


def main():

    x1 = sinwave(A1 , f1)

    N = 4096

    # Multiplicar por um numero grande para aumentar o numero "empurrar a virgula"
    x1Int = np.int16(x1 * 2 ** 13)

    
    plt.figure(facecolor='w', figsize=(20, 30))
    plt.plot(t[0 : 1010], x1[0 : 1010], 'k')
    plt.title('Sinal')
    plt.axis('tight')

    plt.xlabel(r'$t$ (segundos)')
    plt.ylabel('Intensidade')
    plt.savefig("lab2ex1_Sinal.png", bbox_inches='tight', transparent = False)
    plt.show()

    # Ouvir o som. Nao e' obrigatorio

    soundPlay.soundPlay(x1 , fs)

    filename = 'x1.wav'
    wavfile.write(filename, fs , x1Int)

    

    xfft = np.fft.fft(x1[0 : N])

   
    freq1 = np.fft.fftfreq(len(xfft)) * fs
    x1mag = np.abs(xfft) / N

    Xfase = np.angle(xfft)
    
    #espectro amplitude
    plt.figure(facecolor = 'w', figsize=(10 , 20))
    
    plt.stem(freq1, x1mag, 'k', linewidth=3)

    plt.axis([-1100 , 1100 , 0 , 2])
    plt.ylabel('Espectro amplitude', fontsize = 18)
    plt.xlabel('f(Hz)', fontsize = 18)
    plt.xticks(fontsize = 22)
    plt.yticks(fontsize = 22)
    plt.grid()
    plt.savefig("lab2ex1_espectroAmplitude.png", bbox_inches='tight', transparent = False)
    plt.show()
    
    #espectro fase
    plt.figure(facecolor = 'w' , figsize=(30 , 20))
    plt.stem(freq1, Xfase, 'k', linewidth = 3)
    plt.axis([-1100 , 1100 , -np.pi , np.pi])

    plt.ylabel('Espectro de fase', fontsize = 18)
    plt.xlabel('f(Hz)', fontsize = 18)
    plt.xticks(fontsize = 22)
    plt.yticks(fontsize = 22)
    plt.grid()
    plt.savefig("lab2ex1_espectroFase.png" , bbox_inches = 'tight' , transparent = False)
    plt.show()

    
    plt.figure(facecolor = 'w' , figsize = (30 , 20))

    plt.specgram(x1, NFFT=2 * N, Fs = fs, noverlap = 0)
    plt.xlabel('Tempo(s)' , fontsize = 18)
    plt.ylabel('f(Hz)' , fontsize = 18)
    plt.axis([0 , 0.73 , 0 , 1000])
    plt.savefig("lab2ex1_espectrograma.png" , bbox_inches = 'tight' , transparent = False)
    plt.show()


if __name__ == '__main__':
    main()
