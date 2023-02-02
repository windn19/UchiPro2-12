def merge_sort(array):
    print(array)
    if len(array) == 1:
        return array
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    if l >= len(left):
        result += right[r:]
    else:
        result += left[l:]
    return result


array = [1, 4, 0, 3, 2]
print(merge_sort(array))
