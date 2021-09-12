num_list = [3, 4, 2, 5, 1, 6]


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    less = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]
    return quick_sort(less) + middle + quick_sort(greater)


print(quick_sort(num_list))
