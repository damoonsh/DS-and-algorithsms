import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __get_item__(self, k):
        if not (-1 * self._n <= k < self._n):
            raise IndexError('invalid index')

        if k < 0: return self._A[self._n + k]
        
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj

        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    
a = DynamicArray()
a.append(10)
a.append(20)
a.append(30)
a.append(50)
print(a.__get_item__(0))
print(a.__get_item__(-1))
print(a.__get_item__(-4))