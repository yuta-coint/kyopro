import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
n = int(input())
logn = len(bin(n))-1
#iの2**j個先の親を求める。何もない場合は-1を出力する
mother = [[-1 for i in range(n+1)] for j in range(logn)]
G = [[] for i in range(n)]
for i in range(n):
    l = list(map(int,input().split()))
    for k in range(1,l[0]+1):
        mother[0][l[k]] = i
        G[i].append(l[k])
        G[l[k]].append(i)
depth = [-1 for i in range(n)]
d = 0
cnt = 0
stack = [0]
depth[0]=0
while stack:
    v = stack.pop()
    #ord[v] = cnt
    #cnt+=1
    for i in G[v]:
        if depth[i]==-1:
            depth[i] = depth[v]+1
            mother[0][i]=v
            stack.append(i)
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
    for i in reversed(range(logn)):
        if mother[i][u]!=mother[i][v]:
            u = mother[i][u]
            v = mother[i][v]
    if u == v:
        return(u)
    else:
        return(mother[0][u])
q = int(input())
for _ in range(q):
    u,v = map(int,input().split())
    print(LCA(u,v))
    

