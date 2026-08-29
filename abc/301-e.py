H,W,T = map(int,input().split())
A = [["#" for i in range(W+2)]]+[list("#"+input()+"#") for i in range(H)]+[["#" for i in range(W+2)]]
H+=1
W+=1
bis = []
cnt_bis = 0
for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            S = (i,j)
            A[i][j]="."
        if A[i][j]=="G":
            Go = (i,j)
            A[i][j]="."
        if A[i][j]=="o":
            A[i][j]="."
            bis.append((i,j))
            cnt_bis+=1
from collections import deque
def bfs(sx,sy):
    new = deque()
    chk = [0 for i in range(H*W)]
    ans = [-1 for i in range(H*W)]
    t = (sx,sy,0)
    new.appendleft(t)
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
G = [[0 for i in range(cnt_bis+2)] for i in range(cnt_bis+2)]
bis = [S]+bis+[Go]
for i in range(cnt_bis+2):
    temp = bfs(bis[i][0],bis[i][1])
    for j in range(cnt_bis+2):
        G[i][j] = temp[bis[j][0]][bis[j][1]]
#T未満の移動でできる限り多くの種類の点に到達することを目指す。
INF = 10**9
ans = [[INF for j in range(cnt_bis+2)] for i in range(2**cnt_bis)]
ans[0][0]=0
for i in range(2**(cnt_bis+2)):
    for j in range(cnt_bis+2):
        if i&(2**j)!=0:
            for k in range(cnt_bis+2):
                if G[k][j]==0:
                    continue
                temp = ans[i-(2**j)][x[0]]+x[1]
                if temp<ans[i][j]:
                     ans[i][j]=temp
