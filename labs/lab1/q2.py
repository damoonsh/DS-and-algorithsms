# Damoon Shah Hosseini
def arrange_array(arr):
    index, new_arr = 0, []

    while index < len(arr):
        if arr[index] % 2 == 0:
            new_arr.append(arr[index])
            del arr[index]
        else:
            index += 1

    return new_arr + arr