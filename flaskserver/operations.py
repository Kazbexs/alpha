import itertools

def is_independent(s, independent):
    if len(s) == 1:
        return True
    else:
        s_all = itertools.combinations(s, 2)
        for pair in s_all:
            if pair not in independent:
                return False
        return True


def is_causal(s, causal):
    set_a, set_b = s[0], s[1]
    s_all = itertools.product(set_a, set_b)
    for pair in s_all:
        if pair not in causal:
            return False
    return True


def issubset(set_a, set_b):  # help function to check whether the set A is a subset of set B using the A.issubset(B) function 
    if set(set_a[0]).issubset(set_b[0]) and set(set_a[1]).issubset(set_b[1]):
        return True
    return False