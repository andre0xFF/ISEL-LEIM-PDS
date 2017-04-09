[![Build Status](https://travis-ci.com/andrewfonseca/PDS.svg?token=xhSvC9MhC41fwpYgqaqf&branch=master)](https://travis-ci.com/andrewfonseca/PDS)

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

```python
# amplitude
A = 0.8
# frequency
f0 = 10000
# initial phase
phi = np.pi / 2
# sampling rate
fs = 44100
# time axis
t = np.arange(-0.002, 0.002, 1 / fs)
# sinusoid
x = A * np.cos(2 * np.pi * f0 * t + phi)

plt.plot(t, x)
plt.axis([-0.002, 0.002, -0.8, 0.8])
plt.xlabel('time')
plt.ylabel('amplitude')

plt.show()
```

# Complex sinewaves

```python
# size of DFT
n = 500
# frequency / 3 periods
k = 3
# time indexes
t = np.arange(-n/2, n/2)
# complex sinewave
s = np.exp(1j * 2 * np.pi * k * t / n)

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
n = 64
# frequency
k0 = 7

x = np.exp(2 * np.pi * k0 / n * np.arange(n))
_x = np.array([])

nv = np.arange(-n / 2, n / 2)
kv = np.arange(-n / 2, n / 2)

for k in kv:
	s = np.exp(1j * 2 * np.pi * k / n * nv)
	_x = np.append(_x, sum(x * np.conjugate(s)))

plt.plot(kv, abs(X))
plt.axis([- n / 2, n / 2 - 1, 0 , n])
plt.show()
```
# IDFT (inverse)

<a href="https://www.codecogs.com/eqnedit.php?latex=x[n]=\frac{1}{N}&space;\sum_{k=0}^{N-1}&space;X[k]&space;e^{j&space;2&space;\pi&space;k&space;n&space;/&space;N},&space;n=0,&space;1,&space;...,&space;N-1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x[n]=\frac{1}{N}&space;\sum_{k=0}^{N-1}&space;X[k]&space;e^{j&space;2&space;\pi&space;k&space;n&space;/&space;N},&space;n=0,&space;1,&space;...,&space;N-1" title="x[n]=\frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j 2 \pi k n / N}, n=0, 1, ..., N-1" /></a>

```python
import numpy as np
import matplotlib.pyplot as plt

# signal size
n = 64
# frequency
k0 = 7

x = np.exp(2 * np.pi * k0 / n * np.arange(n))
_x = np.array([])

nv = np.arange(-n / 2, n / 2)
kv = np.arange(-n / 2, n / 2)

for k in kv:
	s = np.exp(1j * 2 * np.pi * k / n * nv)
	_x = np.append(_x, sum(x * np.conjugate(s))

y = np.array([])
for _n in nv:
	s = np.exp(1j * 2 * np.pi * _n / n * kv)
	y = np.append(y, 1.0 / sum(x * s))

plt.plot(kv, y)
plt.axis([- n / 2, n / 2 - 1, -1, 1])
plt.show()
```
