import sys
sys.setrecursionlimit(10**7)
N,M = map(int,input().split())
def out(n,s,l):
    if n==0:
        print(*s)
    else:
        for i in range(l,M+1):
            out(n-1,s+[i],i+1)
out(N,[],1)