import reader
import itertools
import relations
import operations
import copy

def find_Tl(log):  # first step - find all possible activities in event-log
    tl = set()
    
    for trace in log:
        for activity in trace:
            tl.update(activity)

    return tl


def find_Ti(log):  # second step - find all start activities - initial elements of each tupel in log
    ti = set()

    for trace in log:
        ti.add(trace[0])

    return ti


def find_To(log):  # third step - find all end activities - final elements of each tupel in log
    to = set()

    for trace in log:
        to.add(trace[-1])

    return to


def find_Xl(tl, independent, causal):  # fourth step - every element of B are causally related and all elements in A and all elements in B are idependent
    xl = set()
    #allPossiblePairs = set(itertools.product(find_Tl(log), repeat=2)) 
    
    #for pair in allPossiblePairs:
    #    if pair in causal:
    #            xl.add(pair)
                
    #allPossibleCombinations = set(itertools.chain.from_iterable((itertools.combinations(find_Tl(log), r) for r in range(1,relations.define_max_length(log) +1 ))))
    
    allPossibleCombinations = set(itertools.chain.from_iterable(itertools.combinations(tl, r) for r in range(1, len(tl) + 1)))
   
    independent_a_or_b = set(
        a_or_b for a_or_b in allPossibleCombinations if operations.is_independent(a_or_b, independent))
    
    for pair in itertools.product(independent_a_or_b, independent_a_or_b):
        if operations.is_causal(pair, causal):
            xl.add(pair)
    
    return xl


def find_Yl(xl, parallel):  # fifth step - find pairs that are subsets of other pairs
    yl = copy.deepcopy(xl)
    s_all = itertools.combinations(yl, 2)
    for p in s_all:
        if operations.issubset(p[0], p[1]):
            yl.discard(p[0])
        elif operations.issubset(p[1], p[0]):
            yl.discard(p[1])

    self_loop = set()  
    for p in parallel:
        if p == p[::-1]:
            self_loop.add(p[0])

    to_be_deleted = set()
    for p in yl:
        if any(j == i[0] for i in p for j in self_loop):
            to_be_deleted.add(p)
    for p in to_be_deleted:
        yl.discard(p)
    return yl
    
      
def generate_alpha(data):
    r = reader.read_data(data)
    tl = find_Tl(r)
    ti = find_Ti(r)
    to = find_To(r)
    ds = relations.find_directly_follows(r)
    cs = relations.find_causal(ds)
    pr = relations.find_parallel(ds)
    ind = relations.find_independent(tl, ds)
    xl = find_Xl(tl, ind, cs)
    yl = find_Yl(xl, pr)

    result_dictionary = {
       "tl": tl,
       "ti": ti,
       "to": to,
       "ds": ds,
       "cs": cs,
       "pr": pr,
       "ind": ind,
       "xl": xl,
       "yl": yl
    }
    return result_dictionary
   