nn = 101
fa = [1] * (nn+1)
for i in range(nn):
    fa[i+1] = fa[i] * (i+1)
def kth_permutation(n, k):
    S = [i for i in range(n)]
    L = []
    for i in range(n):
        a = fa[n-1-i]
        j = k // a
        k %= a
        L.append(S[j])
        S = S[:j] + S[j+1:]
    return L
 
def id_of_permutation(L):
    ret = 0
    while len(L) > 1:
        a = len([l for l in L if l < L[0]])
        ret += a * fa[len(L) - 1]
        L = L[1:]
    return ret