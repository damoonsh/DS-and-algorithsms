

def heap_helper(arr, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and arr[left] < arr[largest]:
        largest = left

    if right < heap_size and arr[right] < arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heap_helper(arr, largest, heap_size)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heap_helper(arr, i, n)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_helper(arr, 0, i)

    return arr


nums = [
    ["a", "c", "x", "A", "X", "b", "B"],
    ["A", "x", "C"],
    ["B", "b", "c", "a", "D", "g"],
    ["a", "A", "B", "X", "c"]
]

for num in nums:
    print(heapsort(num))