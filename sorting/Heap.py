

def heap_data(arr, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and arr[left] < arr[largest]:
        largest = left

    if right < heap_size and arr[right] < arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heap_data(arr, largest, heap_size)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heap_data(arr, i, n)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_data(arr, 0, i)

    return arr


nums = ["a", "c", "x", "A", "X", "b", "B"]
heapsort(nums)
print(nums)

def heap_data(nums, index, heap_size):
    largest_num = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and nums[left_index] < nums[largest_num]:
        largest_num = left_index

    if right_index < heap_size and nums[right_index] < nums[largest_num]:
        largest_num = right_index
    
    if largest_num != index:
        nums[largest_num], nums[index] = nums[index], nums[largest_num]
        heap_data(nums, largest_num, heap_size)

def heap_sort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heap_data(nums, i, n)
        
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heap_data(nums, 0, i)

    return nums
    
# nums = [99, 67, 88, 110, 105]
nums = ["a", "c", "x", "A", "X", "b", "B"]
heap_sort(nums)
print(nums)

nums = ["a", "c", "x", "A", "X", "b", "B"]
heap_sort(nums)
print(nums)