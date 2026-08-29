import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
n = int(input())
logn = len(bin(n))-1
#iの2**j個先の親を求める。何もない場合は-1を出力する
mother = [[-1 for i in range(n+1)] for j in range(logn)]
G = [[] for i in range(n)]
for i in range(n-1):
    x,y = map(int,input().split())
    G[x-1].append(y-1)
    G[y-1].append(x-1)
check = [0 for i in range(n)]
depth = [0 for i in range(n)]
def dfs(v):
    global d
    global depth
    check[v]=1
    for i in G[v]:
        if check[i]==0:
            d += 1
            depth[i] = d
            mother[0][i]=v
            dfs(i)
            d -= 1
d = 0
dfs(0)
for i in range(1,logn):
    for j in range(n):
        mother[i][j]=mother[i-1][mother[i-1][j]]
def LCA(u,v):
    if depth[u]>depth[v]:
        u,v = v,u
    gap = depth[v]-depth[u]
    f = 0
    while gap>0:
        if gap&1:
            v = mother[f][v]
        gap>>=1
        f+=1
    cnt = logn
    for i in reversed(range(logn)):
        if mother[i][u]!=mother[i][v]:
            u = mother[i][u]
            v = mother[i][v]
    if u == v:
        return(u)
    else:
        return(mother[0][u])
q =  int(input())
for i in range(q):
    a,b = map(int,input().split())
    lca = LCA(a-1,b-1)
    ans = depth[a-1]+depth[b-1]-depth[lca]*2+1
    print(ans)