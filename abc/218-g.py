import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from array import array
import bisect
N = int(input())
A = list(map(int,input().split()))
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(lambda x:int(x)-1,input().split())
    G[u].append(v)
    G[v].append(u)
med = [0 for i in range(N)]
unvisited = [True for i in range(N)]
current = array('i',[-1])
depth = 0
bottom = [True for i in range(N)]
def dfs(v,depth,L):
    if depth == 1:
        med[v] = -1
    else:
        med[v] = 10**9+10
    unvisited[v]=False
    bisect.insort(current,A[v])
    for i in G[v]:
        if unvisited[i]:
            dfs(i,depth^1,L+1)
            if depth==1:
                med[v] = max(med[v],med[i])
            else:
                med[v] = min(med[v],med[i])
            bottom[v] = False
    #底だったら
    if bottom[v]:
        if L&1:
            med[v] = current[L//2+1]
        else:
            med[v] = (current[L//2]+current[L//2+1])//2
    #print(bisect.bisect_left(current,A[v]))
    current.pop(bisect.bisect_left(current,A[v]))
dfs(0,1,1)
print(med[0])