from heapq import heappush, heappop
INF = 10 ** 9
V,E = map(int,input().split())
G = [[]for i in range(V)]
for i in range(E):
    a,b = map(lambda x:int(x)-1,input().split())
    G[a].append(b)
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
        ans = [g]
        for i in range(dist[g]):
            ans.append(mother[ans[-1]])
        ans1 = [ans[dist[g]-i] for i in range(dist[g]+1)]
        return(ans1)
