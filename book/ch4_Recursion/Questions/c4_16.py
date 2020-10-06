def reverse(s):
    if len(s) == 1:
        return s
    elif len(s) == 2:
        return s[-1] + s[0]
    
    return s[-1] + reverse(s[1:len(s) - 1]) + s[0]