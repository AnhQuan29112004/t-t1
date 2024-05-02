from sympy import *
def permutations(a):
    n = len(a)
    if n == 1 : return [a]
    G = []
    for i in range(n):
        k = a.copy()
        x = k.pop(i)
        for p in permutations(k):
            p = [x] + p 
            G.append(a)
    return G
print(permutations([1,9,8]))





import itertools
print(list( itertools.permutations([1,2,3])))