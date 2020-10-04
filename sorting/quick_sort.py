"""
    Data Structures and Algorithms, Chapter 12 section 3
"""

def quick_sort(l):
    inplace_quick_sort(l, 0, len(l) - 1)

def inplace_quick_sort(S, a, b):
    """
        S: the sequence to be sorted
        a: the leftmost index
        b: the right most index
    """
    if a >= b: return

    pivot = S[b]
    left = a
    right = b - 1

    while left <= right:
        while left <= right and S[left] < pivot: left += 1

        while left <= right and S[right] > pivot: right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
    
    # Put pivot into its final index
    S[left], S[b] = S[b], S[left]

    # Recursice calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)