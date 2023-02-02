import time

import matplotlib.pyplot as plt


def binary(array, x):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] == x:
            print(mid)
            break
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid
    else:
        print(-1)


result = []
for i in range(10, 10000):
    t = time.time()
    binary(list(range(1, i)), i - 1)
    result.append(time.time() - t)
plt.plot(list(range(10, 10000)), result)
plt.show()
