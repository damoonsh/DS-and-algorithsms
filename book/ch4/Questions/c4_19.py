
def evenize(l: list, index: int = 0) -> list:
    if len(l) == index: return l
    
    if l[index] % 1 == 0:
        l.append(l[index])
        del l[index]
    
    return evenize(l, index + 1)