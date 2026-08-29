import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int,input().split()))
G = [set() for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    G[v-1].add(u-1)
    G[u-1].add(v-1)
import bisect
LIS = [-1]
save = []
cnt = 0
visited = [False for i in range(N)]
ans = [0 for i in range(N)]
def dfs(v):
    global cnt
    visited[v]=True
    if A[v] > LIS[-1]:
        LIS.append(A[v])
        save.append(-1)
        cnt+=1
    else:
        temp = bisect.bisect_left(LIS, A[v])
        save.append((temp,LIS[temp]))
        LIS[temp] = A[v]
    ans[v] = cnt
    for i in G[v]:
        if visited[i]==False:
            dfs(i)
    s = save.pop()
    if s==-1:
        LIS.pop()
        cnt-=1
    else:
        LIS[s[0]]=s[1]
dfs(0)
for i in range(N):
    print(ans[i])