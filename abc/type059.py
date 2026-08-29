N,M,Q  =map(int,input().split())
ans = []
import sys
input = sys.stdin.readline
G = [[] for i in range(N)]
for i in range(M):
    x,y =map(int,input().split())
    G[y-1].append(x-1)
for i in range(N):
    bs = 1<<i
    for v in G[i]:
        bs|=ans[v]
    ans.append(bs)
for _ in range(Q):
    a,b = map(int,input().split())
    if ans[b-1]>>(a-1)&1:
        print("Yes")
    else:
        print("No")