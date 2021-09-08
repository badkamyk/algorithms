num_list = [1, 3, 2, 4, 6, 5]

def count(arr):
    if len(arr) == 0:
          return 0
    else:
          return 1 + count(arr[1:])

# print(count(num_list))          

def add(arr):
    if len(arr) == 0:
          return 0
    else:
          return arr[0] + add(arr[1:])

# print(add(num_list))          

def max(arr):
    if len(arr) == 2:
          return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max(num_list))
