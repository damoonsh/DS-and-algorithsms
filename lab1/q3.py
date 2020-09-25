# Damoon Shah Hosseini
import sys

data = []
capacity = sys.getsizeof(data)

for k in range(1,50):
    a = len(data)
    b = sys.getsizeof(data)
    if b != capacity:
        capacity = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)