from heapq import heappush, heappop
INF = 10 ** 9
V,E = map(int,input().split())
G = [[]for i in range(V)]
Edge = [[0 for i in range(V)] for j in range(V)]
for i in range(E):
    a,b = map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    Edge[a][b]=i
def ShortestRoute(s,g):
    dist = [-1] * V
    hq = [(0, s)] #(distance, node)
    dist[s] = 0
    mother = [-1 for i in range(V)]
    while hq!=[]:
        v = heappop(hq)[1] # ノードを pop する
        #print(v)
        for i in G[v]: # ノード v に隣接しているノードに対して
            if dist[i]==-1:
                dist[i] = dist[v] + 1
                mother[i]=v
                heappush(hq, (dist[i], i))
         #print(dist)
    if dist[g] == INF:
        return(-1)
    else:
        a = [g]
        for i in range(dist[g]):
            a.append(mother[a[-1]])
        ans1 = [a[dist[g]-i] for i in range(dist[g]+1)]
        return(ans1)
def bfsdj(_):
    dist = [-1] * V
    hq = [(0, 0)] #(distance, node)
    dist[0] = 0
    while hq!=[]:
        v = heappop(hq)[1] # ノードを pop する
        #print(v)
        for i in G[v]: # ノード v に隣接しているノードに対して
            if dist[i]==-1:
                dist[i] = dist[v] + 1
                heappush(hq, (dist[i], i))
        #print(dist)
    return(dist[V-1])
normal = ShortestRoute(0,V-1)
if normal == -1:
    ans = [-1 for i in range(E)]
else:
    ans = [len(normal)-1 for i in range(E)]
    for i in range(len(normal)-1):
        G[normal[i]].remove(normal[i+1])
        ans[Edge[normal[i]][normal[i+1]]] = bfsdj(0)
        G[normal[i]].append(normal[i+1])
for i in ans:
    print(i)
