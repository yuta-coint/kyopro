import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
G = [set() for i in range(2*N)]
import queue
dist = [float("inf") for i in range(2*N)]
for i in range(M):
    u,v,a = map(int,input().split())
    u-=1
    v-=1
    a =1-a
    G[u*2+a].add(v*2+a)
    G[v*2+a].add(u*2+a)
s = list(map(int,input().split()))
s = set(s)
visited = [False for i in range(2*N)]
q = queue.Queue()
visited[0]=True
dist[0]=0
q.put(0)
if 1 in s:
    q.put(1)
    dist[1]=0
while not q.empty():
    v = q.get()
    for i in G[v]:
        if visited[i]:
            continue
        visited[i]=True
        dist[i]=dist[v]+1
        if (i>>1)+1 in s:
            if not (visited[i^1]):
                dist[i^1]=dist[i]
                q.put(i^1)
        q.put(i)
#print(dist)
if dist[2*N-1]==float("inf") and dist[2*N-2]==float("inf"):
    print(-1)
else:
    print(min(dist[2*N-1],dist[2*N-2]))
