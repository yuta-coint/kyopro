import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)
import copy
V = int(input())
p = list(map(lambda x:int(x)-1,input().split()))
#i番目がどこにあるか
q = [0 for i in range(V)]
for i in range(V):
    q[p[i]]=i
ans = []
E = int(input())
G = [[0 for i in range(V)] for i in range(V)]
G1 = [[] for i in range(V)]
edge = [[0 for i in range(V)] for i in range(V)]
for i in range(E):
    u,v = map(lambda x:int(x)-1 ,input().split())
    G[u][v]=1
    G[v][u]=1
    G1[u].append(v)
    G1[v].append(u)
    edge[u][v]=i
    edge[v][u]=i
for i in G1:
    i = set(i)
import queue
unvisited = [True for i in range(V)]
#揃える順番を決める
orde = []
def dfs(v):
    global unvisited
    unvisited[v] = False
    for i in G1[v]:
        if unvisited[i]:
            dfs(i)
    orde.append(v)
for t in range(V):
    if unvisited[t]:
        dfs(t)

#sからgまでのルート表示
def find_route(s,g):
    stack = []
    check = copy.copy(gcheck)
    stack.append(s)
    check[s]=1
    while stack!=[]:
        v = stack[-1]
        if v == g:
            return stack # stack には2頂点間の経路が入っている
        else:
            unvisited = 0
            for k in G1[v]:
                if G[v][k]>0 and check[k]==0:
                    unvisited = 1
                    check[k]=1
                    stack.append(k)
                    break
            if unvisited==0:
                stack.pop()
    return(-1)
#print(find_route(5,2))
gcheck = [0 for i in range(V)]
for i in orde:
    r = find_route(i,q[i])
    if r==-1:
        break
    for j in reversed(range(len(r)-1)):
        f = r[j]
        u = r[j+1]
        ans.append(edge[f][u])
        p[f],p[u]=p[u],p[f]
        q[p[f]],q[p[u]]=q[p[u]],q[p[f]]
    gcheck[i]=1

ideal = [i for i in range(V)]
for i in range(len(ans)):
    ans[i]+=1
if ideal==p:
    print(len(ans))
    print(*ans)
else:
    print(-1)