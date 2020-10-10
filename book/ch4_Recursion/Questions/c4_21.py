
def check(S:list, index1: int, index2: int, target: int): 
    if index1 == len(S): return None
    
    Sum = S[index1] + S[index2]
    
    if Sum > target:
        return None
    elif Sum < target:
        if index2 + 1 == len(S):
            return check(S, index1 + 1, index1 + 2, target)
        else:
            return check(S, index1, index2 + 1, target)
    else:
        return (S[index1], S[index2])