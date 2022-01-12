import numpy as np
import matplotlib.pyplot as plt

# Recursive euler method
def euler(y0, x0, h, n):
    return get_yn(y0, x0-h, h, n)

def get_yn(y0, x0, h, n):
    if(n == 0):
        return y0
    else:
        x0 = x0 + h
        n = n - 1
        yn = get_yn(y0, x0, h, n)
        return round((yn + h * F(yn, x0)), 4);

# END EULER METHOD

def F(y0, x0):
    return y0

f = lambda x, y: y
h = 0.1
x = np.arange(0, 1 + h, h)
y0 = 1
y = np.zeros(len(x))
y[0] = y0

for i in range(1, len(x)): y[i] = euler(1, 0, h, i)

h2 = 0.05
x2 = np.arange(0, 1 + h2, h2)
y2 = np.zeros(len(x2))
y2[0] = y0

for i in range(1, len(x2)): y2[i] = euler(1, 0, h2, i)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo--', label='Approximation h = 0.1')
plt.plot(x2, y2, 'bo--', label='Approximation h = 0.05', color='green')
plt.plot(x, np.exp(x), 'g', label='Exact', color='black')
plt.title('Approximate and Exact Solution: \
h = 0.1')

plt.xlabel('X')
plt.ylabel('F(x)')
plt.grid()
plt.legend(loc='lower right')
plt.show()