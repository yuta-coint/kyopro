import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
H,W = map(int,input().split())
visited = [[False for j in range(W)] for i in range(H)]
C = [input() for i in range(H)]
for i in range(H):
    for j in range(W):
        if C[i][j]=="S":
            St = (i,j)
ans = "No"
from collections import deque
def dfs(vi,vj):
    global ans
    S = deque()
    S.append((vi,vj,0))
    while S:
        vi,vj,depth = S.pop()
        if visited[vi][vj]:
            continue
        visited[vi][vj]=True
        for  i,j in [(vi,vj-1),(vi,vj+1),(vi+1,vj),(vi-1,vj)]:
            if i==-1 or j==-1 or i==H or j==W:
                continue
            if (i,j)==St and depth>1:
                ans="Yes"
            if visited[i][j]:
                continue
            if C[i][j]=="#":
                continue
            S.append((i,j,depth+1))
dfs(St[0],St[1])
print(ans)