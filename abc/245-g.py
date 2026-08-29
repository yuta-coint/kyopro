import sys
input = sys.stdin.readline
N,M,K,L = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(lambda x:int(x)-1,input().split()))
G = [[] for i in range(N)]
for i in range(M):
    u,v,c = map(int,input().split())
    u-=1
    v-=1
    G[u].append((c,v))
    G[v].append((c,u))
from distutils import dist
from heapq import heapify,heappop,heappush
dist1 = [float('inf') for i in range(N)]
mother = [None for i in range(N)]#一番近い人の国籍
dist2 = [float('inf') for i in range(N)]#その国籍以外で一番近い人
q = []
heapify(q)
seen = [-1] * N # ノードが確定済みかどうか
for i in b:
    heappush(q,(0,i,a[i]))
    dist1[i]=0
    mother[i]=a[i]
while q!=[]:
    d,v,home = heappop(q)
    #print(d,v,home)
    #その頂点がすでにふたつとも確定済みであればcontinueする。
    if seen[v]==-2:
        continue
    if seen[v]==home:
        continue
    if seen[v]==-1:
        seen[v]=home
    else:
        seen[v]=-2
    for i in G[v]:
        if seen[i[1]]==-2:
            continue
        if seen[i[1]]==-1:
            #何も確定していないので二段階の比べ合いをする。
            if d+i[0]<=dist1[i[1]]:
                if home!=mother[i[1]]:
                    dist2[i[1]]=dist1[i[1]]
                    mother[i[1]]=home
                dist1[i[1]]=d+i[0]
                heappush(q,(dist1[i[1]],i[1],home))
            elif d+i[0]<dist2[i[1]] and home!=mother[i[1]]:
                dist2[i[1]]=d+i[0]
                heappush(q,(dist2[i[1]],i[1],home))
        else:
            if d+i[0]<dist2[i[1]] and home!=mother[i[1]]:
                dist2[i[1]]=d+i[0]
                heappush(q,(dist2[i[1]],i[1],home))
#print(dist1)
#print(dist2)
#print(mother)
ans = []
for i in range(N):
    if mother[i]==a[i]:
        ans.append(dist2[i])
    else:
        ans.append(dist1[i])
    if ans[i]==float('inf'):
        ans[i]=-1
print(*ans)


