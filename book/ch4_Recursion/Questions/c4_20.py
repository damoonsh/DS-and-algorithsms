
def c(S: list, k: int, index: int = 0, changes=0):
    if index == len(S) - changes: return S
    
    if S[index] > k:
        S.append(S[index])
        del S[index]
        changes += 1
    else:
        index += 1
    
    return c(S, k, index, changes)