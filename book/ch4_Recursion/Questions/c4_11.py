def multiply(m, n):
    if n == 0: return 0
    return m + multiply(m, n - 1)

