from math import factorial

import numpy as np
from matplotlib import pyplot as plt


x = list(range(1, 100))
y0 = [10 for _ in x]
y = np.log(x)
y1 = x
y2 = x * np.log(x)
y3 = [x1 ** 2 for x1 in x]
# y4 = [2 ** x1 for x1 in x]
# y5 = [factorial(x1) for x1 in x]
plt.plot(x, y0, label='const')
plt.plot(x, y, label='log n')
plt.plot(x, y1, label='x')
plt.plot(x, y2, label='n log n')
plt.plot(x, y3, label='x ^ 2')
# plt.plot(x, y4, label='2 ^ x')
# plt.plot(x, y5, label='x!')
plt.legend()
plt.xlabel('Количество элементов')
plt.ylabel('Число операций')
plt.ylim(0, 100)
plt.xlim(0, 100)
plt.show()
