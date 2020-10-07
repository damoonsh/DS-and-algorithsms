# Damooon Shah Hosseini - 500963509

def bubble(arr):
    for index in range(len(arr) - 1, 0, -1):
        for j in range(index):
            if ord(arr[j]) < ord(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def insertion(arr):
    for index in range(1, len(arr)):
        current_val = arr[index]
        pos = index

        while pos > 0 and arr[pos - 1] < current_val:
            arr[pos] = arr[pos - 1]
            pos -= 1

        arr[pos] = current_val
    
    return arr

def selection(arr):
    for reach in range(len(arr) - 1, 0, -1):
        max_index = 0

        for index in range(1, reach + 1):
            if arr[index] < arr[max_index]: max_index = index

        arr[reach], arr[max_index] = arr[max_index], arr[reach]
    
    return arr