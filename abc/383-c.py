H,W,D = map(int,input().split())
A = [["#" for i in range(W+2)]]+[list("#"+input()+"#") for i in range(H)]+[["#" for i in range(W+2)]]
H+=2
W+=2
#(sy,sxからの距離を出力)
from collections import deque
def bfs(starts):
    new = deque()
    chk = [0 for i in range(H*W)]
    ans = [-1 for i in range(H*W)]
    for sx,sy in starts:
        new.appendleft((sx,sy,0))
        chk[sx*W+sy]=1
    counter = 0
    while new:
        px,py,counter = new.pop()
        if ans[px*W+py]!=-1:
            continue
        ans[px*W+py]=counter
        counter+=1
        if A[px-1][py]=="." and chk[px*W+py-W]==0:
            new.appendleft((px-1,py,counter))
            chk[px*W+py-W]=1
        if A[px+1][py]=="." and chk[px*W+py+W]==0:
            new.appendleft((px+1,py,counter))
            chk[px*W+py+W]=1
        if A[px][py-1]=="." and chk[px*W+py-1]==0:
            new.appendleft((px,py-1,counter))
            chk[px*W+py-1]=1
        if A[px][py+1]=="." and chk[px*W+py+1]==0:
            new.appendleft((px,py+1,counter))
            chk[px*W+py+1]=1
    return(ans)
S = []
for i in range(H):
    for j in range(W):
        if A[i][j]=="H":
            S.append((i,j))
dists = bfs(S)
fin_ans = 0
for i in range(H*W):
    if 0<=dists[i]<=D:
        fin_ans+=1
print(fin_ans)