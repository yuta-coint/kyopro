N = int(input())
import sys
input = sys.stdin.readline
ax,ay = map(lambda x:int(x)-1,input().split())
bx,by = map(lambda x:int(x)-1,input().split())
S = [input() for i in range(N)]
dist = [[[float('inf') for i in range(N)] for j in range(N)] for _ in range(4)]
unvisited = [[[True for i in range(N)] for j in range(N)] for _ in range(4)]
from collections import deque
q = deque()
for i in range(4):
    q.append((i,ax,ay))
    dist[i][ax][ay]=1
while q:
    d,x,y = q.pop()
    #print(d,x,y,dist[d][x][y])
    #print(x,y,t)
    if unvisited[d][x][y]==False:
        continue
    unvisited[d][ax][ay] = False
    pm = [(1,1),(1,-1),(-1,1),(-1,-1)]
    if 0<=x+pm[d][0]<N and 0<=y+pm[d][1]<N:
        if dist[d][x+pm[d][0]][y+pm[d][1]]>dist[d][x][y] and S[x+pm[d][0]][y+pm[d][1]]=='.':
            q.append((d,x+pm[d][0],y+pm[d][1]))
            dist[d][x+pm[d][0]][y+pm[d][1]]=dist[d][x][y]
    for i in range(4):
        if dist[i][x][y]>dist[d][x][y]+1:
            q.appendleft((i,x,y))
            dist[i][x][y]=dist[d][x][y]+1
ans = min(dist[0][bx][by],dist[1][bx][by],dist[2][bx][by],dist[3][bx][by])
if ans==float('inf'):
    print(-1)
else:
    print(ans)