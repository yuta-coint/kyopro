N,X,Y = map(int,input().split())
G = [set() for i in range(N)]
for i in range(N-1):
    u,v  = map(lambda x:int(x)-1,input().split())
    G[u].add(v)
    G[v].add(u)

import queue
dist = [float("inf") for i in range(N)]
visited = [False for i in range(N)]
mother = [-1 for i in range(N)]
q = queue.Queue()
visited[Y-1]=True
dist[Y-1]=0
q.put(Y-1)
while not q.empty():
    v = q.get()
    for i in G[v]:
        if visited[i]:
            continue
        visited[i]=True
        dist[i]=dist[v]+1
        mother[i]=v
        q.put(i)
ans = []
now = X-1
while now!=-1:
    ans.append(now+1)
    now = mother[now]
print(*ans)