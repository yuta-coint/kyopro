import sys
input = sys.stdin.readline
from heapq import heappush, heappop
h,w,t = map(int,input().split())
G = [list(input()) for i in range(h)]
for i in range(h):
    for j in range(w):
        if G[i][j]=="S":
            Start0=i
            Start1=j
        elif G[i][j]=="G":
            goal0 = i
            goal1 = j
def dj(x):
    seen = [[False]*w for _ in range(h)]
    dist = [[float("inf")]*w for _ in range(h)]
    dist[Start0][Start1]=0
    hq = [(0,Start0,Start1)]
    while hq!=[]:
        v = heappop(hq)
        vh = v[1]
        vw = v[2]
        seen[vh][vw]=True
        for vi in [(vh-1,vw),(vh+1,vw),(vh,vw-1),(vh,vw+1)]:
            if vi[0]==-1 or vi[1]==-1 or vi[0]==h or vi[1]==w:
                continue
            if G[vi[0]][vi[1]]=="#":
                k = x
            else:
                k = 1
            if seen[vi[0]][vi[1]] == False and dist[vh][vw] + k < dist[vi[0]][vi[1]]:
                dist[vi[0]][vi[1]] = dist[vh][vw] + k
                heappush(hq, (dist[vi[0]][vi[1]],vi[0],vi[1]))
    return(dist[goal0][goal1])
m = 1
M = 1<<60
while m+1<M:
    ans = (m+M)//2
    if dj(ans)<=t:
        m=ans
    else:
        M=ans
print(m)