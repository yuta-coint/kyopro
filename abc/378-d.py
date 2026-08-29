import sys
sys.setrecursionlimit(10**8)
from copy import deepcopy
H,W,K = map(int,input().split())
blocked = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    S = input()
    for j in range(W):
        if S[j]=="#":
            blocked[i][j]=1
#封鎖状況、何マス進んだか、今いる場所
nbd = [(0,-1),(0,1),(-1,0),(1,0)]
ans = 0
def calc(cnt,now):
    i,j = now
    blocked[i][j]=1
    global ans
    #print(B,cnt,now,ans)
    if cnt == K:
        ans+=1
    else:
        for p in nbd:
            x,y = i+p[0],j+p[1]
            if 0<=x<H and 0<=y<W:
                if blocked[x][y]==0:
                    calc(cnt+1,(x,y))
    blocked[i][j]=0
for i in range(H):
    for j in range(W):
        if blocked[i][j]==0:
            #print(blocked)
            calc(0,(i,j))
print(ans)