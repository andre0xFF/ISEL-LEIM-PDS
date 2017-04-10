# Bibliography
https://ccrma.stanford.edu/~jos/mdft/

# Sinusoids
* https://ccrma.stanford.edu/~jos/mdft/Sinusoids.html
* https://ccrma.stanford.edu/~jos/mdft/Example_Sinusoids.html
* https://ccrma.stanford.edu/~jos/mdft/Sinusoid_Magnitude_Spectra.html
* https://ccrma.stanford.edu/~jos/mdft/Complex_Sinusoids.html
* https://ccrma.stanford.edu/~jos/mdft/Positive_Negative_Frequencies.html
* https://ccrma.stanford.edu/~jos/mdft/Sinusoidal_Amplitude_Modulation_AM.html

# Python 3 notes on Fedora 25

## pip
```shell
sudo python3.5 -m pip install --upgrade pip
```

## matplotlib, numpy and scipy
```
sudo dnf install python3-matplotlib python3-numpy python3-scipy
```

Or..

```
sudo python3.5 -m pip install scipy
```

# Python and sounds

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write

# fs sampling rate
(fs, x) = read('./sms-tools/sounds/flute-A4.wav')

# time axis
t = np.arange(x.size/fs)

plt.plot(t, x)

y = x[44100:45100]
plt.plot(y)
plt.show()

np.max(y)
np.max(abs(y))
np.sum(y)

write('test.wav', fs, y)
```

# Sinusoids

<img src="https://latex.codecogs.com/gif.latex?\inline&space;x[n]=Acos(&space;2&space;\pi&space;f&space;n&space;T&space;&plus;&space;\varphi&space;)" title="x[n]=Acos( 2 \pi f n T + \varphi )" />

```python
# amplitude
A = 0.8

# frequency
f0 = 1000

# initial phase
phi = np.pi / 2

# sampling rate
fs = 44100

# time axis (range, range, increment)
# period: T = 1 / f
t = np.arange(-0.002, 0.002, 1 / fs)

# sinusoid
x = A * np.cos(2 * np.pi * f0 * t + phi)

plt.plot(t, x)
plt.axis([-0.002, 0.002, -0.8, 0.8])
plt.xlabel('time')
plt.ylabel('amplitude')

plt.show()
```

<a href="http://ibb.co/c5QFrQ"><img src="http://preview.ibb.co/bBPVQk/figure_1.png" alt="figure_1" border="0"></a>

# Complex sine waves

<img src="https://latex.codecogs.com/gif.latex?\inline&space;S_{k}[n]=e^{j&space;2&space;\pi&space;k&space;n/N}=cos(2&space;\pi&space;k&space;n/N)&plus;jsin(2&space;\pi&space;k&space;n/N)" title="S_{k}[n]=e^{j 2 \pi k n/N}=cos(2 \pi k n/N)+jsin(2 \pi k n/N)" />

Complex sinewaves are the ones that appear in DFT. These are complex sinewaves that are **discrete** and they do not have any time information. So it's just with an index n and the frequencies in integer value. These complex sine waves are always Periodic for a given capital N - **capital N is going to be the size of the DFT.**

These always have a fixed number of periods within that **n** and this depends on **k** - **k is the number of periods within that capital N.**

```python
# size of DFT
N = 500

# frequency / 3 periods
k = 3

# time indexes
n = np.arange(-N / 2, N / 2)

# complex sinewave
s = np.exp(1j * 2 * np.pi * k * t / N)

# real part
plt.plot(t, np.real(s))

plt.axis([-n / 2, n / 2 - 1, -1, 1])
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()

# imaginary part
plt.plot(t, np.imag(s))

plt.show()
```

# DFT (direct)

<a href="https://www.codecogs.com/eqnedit.php?latex=X[k]=\sum_{n=0}^{N-1}&space;X[n]&space;e^{-j&space;2&space;\pi&space;k&space;n&space;/&space;N},&space;k=0,&space;...,&space;N-1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X[k]=\sum_{n=0}^{N-1}&space;X[n]&space;e^{-j&space;2&space;\pi&space;k&space;n&space;/&space;N},&space;k=0,&space;...,&space;N-1" title="X[k]=\sum_{n=0}^{N-1} X[n] e^{-j 2 \pi k n / N}, k=0, ..., N-1" /></a>

```python
import numpy as np
import matplotlib.pyplot as plt

# signal size
N = 64

# frequency
k0 = 7

# real signal
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

X = np.array([])
nv = np.arange(-N / 2, N / 2)
kv = np.arange(-N / 2, N / 2)

for k in kv:
    s = np.exp(1j * 2 * np.pi * k / N * nv)
    X = np.append(X, sum(x * np.conjugate(s)))

plt.plot(kv, abs(X))
plt.axis([- N / 2, N / 2 - 1, 0 , N])
plt.show()
```

# IDFT (inverse)

<a href="https://www.codecogs.com/eqnedit.php?latex=x[n]=\frac{1}{N}&space;\sum_{k=0}^{N-1}&space;X[k]&space;e^{j&space;2&space;\pi&space;k&space;n&space;/&space;N},&space;n=0,&space;1,&space;...,&space;N-1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x[n]=\frac{1}{N}&space;\sum_{k=0}^{N-1}&space;X[k]&space;e^{j&space;2&space;\pi&space;k&space;n&space;/&space;N},&space;n=0,&space;1,&space;...,&space;N-1" title="x[n]=\frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j 2 \pi k n / N}, n=0, 1, ..., N-1" /></a>

```python
import numpy as np
import matplotlib.pyplot as plt

# signal size
N = 64

# frequency
k0 = 7

x = np.exp(2 * np.pi * k0 / N * np.arange(N))

X = np.array([])

nv = np.arange(-N / 2, N / 2)
kv = np.arange(-N / 2, N / 2)

for k in kv:
	s = np.exp(1j * 2 * np.pi * k / N * nv)
	X = np.append(X, sum(x * np.conjugate(s)))

Y = np.array([])

for n in nv:
	s = np.exp(1j * 2 * np.pi * n / N * kv)
	Y = np.append(Y, 1.0 / N * sum(X * s))

plt.plot(kv, Y)
plt.axis([- N / 2, N / 2 - 1, -1, 1])
plt.show()
```
