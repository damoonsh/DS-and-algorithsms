
def perm(arr):
    if len(arr) == 1:
        return [arr]
    else:
        sub = perm(arr[1:])
        main = []

        for elem in sub:
            main.append(elem + [arr[0]])
            main.append(elem)

        main.append([arr[0]])

    return main

print(perm(['a','b','c']))