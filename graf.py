import time


import matplotlib.pyplot as plt


def grafic(func):
    def inner(*args):
        result = []
        for i in range(10, 10000):
            t = time.time()
            func(list(range(1, i)), i - 1)
            result.append(time.time() - t)
        plt.plot(list(range(10, 10000)), result)
        # plt.ylim(-1, 8)
        plt.show()
    return inner


