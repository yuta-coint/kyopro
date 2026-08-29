import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)
import copy
V,E = map(int,input().split())
G = [[0 for i in range(V)] for i in range(V)]
G1 = [[] for i in range(V)]
for i in range(E):
    u,v,c = map(int,input().split())
    G[u][v]=c
    G1[u].append(v)
    G1[v].append(u)
for i in G1:
    i = set(i)
import queue
#0からV-1までのルート表示
def find_route(_):
    stack = []
    #stack = queue.LifoQueue()
    check = [0 for i in range(V)]
    stack.append(0)
    check[0]=1
    while stack!=[]:
        v = stack[-1]
        if v == V-1:
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
#print(find_route(0))
ans = 0
#for i in range(3):
while True:
    route = find_route(0)
    #print(route)
    if route == -1:
        break
    #route.append(V-1)
    m = len(route)
    amount = 10**9
    for i in range(m-1):
        if amount>G[route[i]][route[i+1]]:
            amount = G[route[i]][route[i+1]]
    for i in range(m-1):
        G[route[i]][route[i+1]]-=amount
        G[route[i+1]][route[i]]+=amount
    ans+=amount
print(ans)