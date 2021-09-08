def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
          if smallest > arr[i]:
                smallest = arr[i]
                smallest_index = i
    return smallest_index




def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
          smallest = find_smallest(arr)
          new_arr.append(arr.pop(smallest))
    return new_arr


num_list = [3, 4, 2, 5, 1, 6]

print(selection_sort(num_list))
