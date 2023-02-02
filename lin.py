from graf import grafic


@grafic
def search(arr, x):
    for num, i in enumerate(arr):
        if i == x:
            break


search([], 1)