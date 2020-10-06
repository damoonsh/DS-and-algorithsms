def log2(num):
    if num <= 0 : raise ValueError('Non-positive values cannot be inputed to a logarithm function')

    return log_helper(num, 0)

def log_helper(num, value):
    if num // 2 >= 2:
        return log_helper(num // 2, value + 1)
    else:
        return value + 1

