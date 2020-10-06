def f(arr):
    """ If there were nothing in the array then it should be zero. """
    if len(arr) == 0: return None, None
    return f_helper(arr, arr[0], arr[0])

def f_helper(arr, Max, Min):
    if len(arr) == 0: return Max, Min

    if arr[0] > Max: Max = arr[0]
    if arr[0] < Min: Min = arr[0]

    return f_helper(arr[1:], Max, Min)


a = [10, 1, 3, 100, -10]
print(f(a))
