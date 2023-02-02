import time

import matplotlib.pyplot as plt


def const(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


n = int(input())
print((1 + n) * n // 2)
const(n)


result = []
for i in range(10, 10000):
    t = time.time()
    const(i)
    result.append(time.time() - t)
plt.plot(list(range(10, 10000)), result)
plt.show()
