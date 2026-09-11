import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = 3 * x + 4
y2 = 2 * x ** 2 + 1
y3 = x ** 3 + 9

plt.plot(x, y1, label='y = 3x + 4')
plt.plot(x, y2, label='y = 2x^2 + 1')
plt.plot(x, y3, label='y = x^3 + 9')

plt.legend()
plt.show()