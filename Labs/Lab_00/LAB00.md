File: PDS.Python_Introd_lab1.pdf

Page: 52

# Exercise 01

* The step in np.arange() must be smaller than the period (T)
* Cos and Sin sum. Two oscillations are expected.

## First equation
```python
t1 = np.arange(0, 2 + 1, 0.01)
x1 = np.cos(2 * np.pi * t1 + np.pi / 4) + 1 / 5 * np.sin(10 * np.pi * t1 - np.pi / 3)
plt.plot(t1, x1)
plt.show()
```

## Second equation
```python
t2 = np.arange(-2, 2 + 1, 0.01)
x2 = np.cos(2 * np.pi * np.power(t2, 2)) + 1 / 3 * np.sin(25 * np.pi * t2)
plt.plot(t2, x2)
plt.show()
```

# Exercise 02

## exp(-n/5)

```python
n = np.arange(-2, 10 + 1)
x = np.zeros(len(n))
x[n >= 0] = np.exp(-1 * n[n >= 0] / 5)

plt.figure()
plt.stem(n, x)
plt.show()
```
## X1[n], X2[n], X3[n], X4[n]
```python
n1 = np.arange(-2, 8 + 1)
x1 = np.zeros(len(n1))
x1[(-1 * n + 3) >= 0] = 1


figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.stem(n1, x1)
ax2.stem(n2, x2)
ax3.stem(n3, x3)
ax4.stem(n4, x4)
```
# Exercise 03
