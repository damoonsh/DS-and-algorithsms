# Damoon Shah Hosseini

# Solution 1
def switch_halves(array):
    return array[len(array) // 2:] + array[:len(array) // 2]

def average_arr(array):
    return sum(array) / len(array)

def halves_averages(array):
    return average_arr(array[:len(array) // 2]), average_arr(array[len(array) // 2:])

# Solution 2
def q1(arr):
    avg1, avg2 = 0, 0

    for i in range(0, len(arr) // 2):
        avg1 += arr[i]

        holder = arr[i]
        arr[i] = arr[len(arr) // 2 + i]
        arr[len(arr) // 2 + i] = holder
    
    avg2 = 2 * (sum(arr) - avg1 ) / len(arr)

    return arr, avg1 * 2 /  len(arr), avg2
