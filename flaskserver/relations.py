import itertools

# help functions to find all relations using the slides : IV. Alpha Algorithm: Log Based Ordering Relations (cf. [1], Def. 6.3)

def find_directly_follows(log):  # a >L b relation
    directlyFollows = set()

    for trace in log:
        directlyFollows.update((itertools.pairwise(trace)))

    return directlyFollows


def find_causal(directlyFollows):  # a ->L b relation
    causal = set()
    reversedDirectlyFollows = reverse_set(directlyFollows)

    for pair in directlyFollows:
        if pair not in reversedDirectlyFollows:
            causal.add(pair)

    return causal


def find_independent(tl, directlyFollows):  # a #L b relation
    independent = set()
    reversedDirectlyFollows = reverse_set(directlyFollows)
    allPossiblePairs = set(itertools.product(tl, repeat=2))
    for pair in allPossiblePairs:
        if pair not in directlyFollows and pair not in reversedDirectlyFollows:
            independent.add(pair)

    return independent


def find_parallel(directlyFollows):  # a ||L b relation
    parallel = set()
    reversedDirectlyFollows = reverse_set(directlyFollows)

    for pair in directlyFollows:
        if pair in reversedDirectlyFollows:
            parallel.add(pair)
    
    return parallel


def reverse_set(setToReverse):  # help function to reverse pairs in set
    result = set()

    for pair in setToReverse:
        result.add(pair[::-1])

    return result

def define_max_length(log):
    maximal = 0
    for i in log:
        if len(i)>maximal:
            maximal= len(i)
    return maximal