import sys
input  =sys.stdin.readline
N,M =map(int,input().split())
P = [0]+list(map(int,input().split()))
G = [[] for i in range(N)]
for i in range(1,N):
    G[P[i]-1].append(i)
d = {i:0 for i in range(N)}
for i in range(M):
    x,y = map(int,input().split())
    if x-1 in d:
        d[x-1]=max(d[x-1],y+1)
    else:
        d[x-1]=y+1
S = []
ans = 0
S.append((0,d[0]))
visited = [False for i in range(N)]
while S:
    per,insu = S.pop()
    if visited[per]:
        continue
    visited[per]=True
    if insu>0:
        ans+=1
    for i in G[per]:
        S.append((i,max(insu-1,d[i])))
print(ans)