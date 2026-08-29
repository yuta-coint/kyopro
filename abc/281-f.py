N = int(input())
import sys
sys.setrecursionlimit(10**7)
a = list(map(int,input().split()))
a.sort()
from functools import lru_cache
@lru_cache(maxsize=None)
def solve(b,l,r):
    one = False
    zero = False
    cut = l-1
    for i in range(l,r):
        if (a[i]>>b)&1:
            one=True
        else:
            zero=True
            cut=i
    if b==0:
        if one and zero:
            return(1)
        else:
            return(0)
    else:
        if one and zero:
            return((1<<b)+min(solve(b-1,l,cut+1),solve(b-1,cut+1,r)))
        else:
            return(solve(b-1,l,r))
print(solve(32,0,N))