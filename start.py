array = list(range(1, 100000))
n = len(array)
x = 99999


for num, i in enumerate(array):
    # print(num, i)
    if x == i:
        print(num)
        break
else:
    print(-1)
