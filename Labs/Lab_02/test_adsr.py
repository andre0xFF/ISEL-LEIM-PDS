#PDSr 2016-17 - Aula Pratica 2 - turma 21

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

#teste geracao ADSR
d = 3
Fs = 10000
t = np.arange(0, d, 1. / Fs)
pAttack = .1
pDecay = .05
pSustain = .80
pRelease = .05
adsr = np.zeros(d*Fs)

t = np.arange(0, d * pAttack, 1. / Fs)
adsr[0:len(t)] = 1. / (d * pAttack) * t

t = np.arange(d * pAttack, d * (pAttack + pDecay), 1. / Fs)
adsr[int(d * pAttack * Fs):int(d * (pAttack + pDecay) * Fs)] = 0.4 * np.exp(-t / (pDecay * d / 5.)) + .6

t = np.arange(d * (pAttack + pDecay), d * (pAttack + pDecay + pSustain), 1. / Fs)
adsr[int(d * (pAttack + pDecay) * Fs):int(d * (pAttack + pDecay + pSustain) * Fs)] = .6
plt.plot(adsr)

t = np.arange(0, d * (pRelease), 1. / Fs)
adsr[int(d * (pAttack + pDecay + pSustain) * Fs):d * Fs] = .6 - (.6 / (pRelease * d)) * t
plt.plot(adsr)


#teste Analise na Frequencia
x = 20000 * np.cos(2 * np.pi * 440. * t)
y = 20000 * np.cos(2 * np.pi * 440 * (2 ** (2. / 12)) * t)
musica = np.hstack((x, y, x, y))
wav.write('teste1.wav', Fs, musica.astype('int16'))

Fs, musica = wav.read('teste1.wav')
plt.plot(musica)
espectro = np.fft.fft(musica)
plt.figure()
spect, f, t, ii = plt.specgram(musica, Fs=Fs, NFFT=512, noverlap=0)
plt.figure()
lista = []

for j in np.arange(0, spect.shape[1], 1):
    plt.plot(f, spect[:, j])
    lista.append(np.argmax(spect[:, j]))
