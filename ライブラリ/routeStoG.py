import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)
import copy
V,E = map(int,input().split())
G = [[0 for i in range(V)] for i in range(V)]
G1 = [[] for i in range(V)]
#有効グラフ仕様になっていることに注意
for i in range(E):
    u,v,c = map(int,input().split())
    G[u][v]=c
    G1[u].append(v)
for i in G1:
    i = set(i)
import queue
#sからgまでのルート表示
def find_route(s,g):
    stack = []
    #stack = queue.LifoQueue()
    check = [0 for i in range(V)]
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