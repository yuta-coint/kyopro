H,W = map(int,input().split())
A = [["#" for i in range(W+2)]]+[list("#"+input()+"#") for i in range(H)]+[["#" for i in range(W+2)]]
H+=2
W+=2
#とりあえず埋めなおす。
emb = set()
big = 10**9
for i in range(H):
    for j in range(W):
        if A[i][j]==">":
            emb.add(i*big+j)
            for k in range(j+1,W):
                if A[i][k]==".":
                    emb.add(i*big+k)
                else:
                    break
        elif A[i][j]=="<":
            emb.add(i*big+j)
            for k in reversed(range(j)):
                if A[i][k]==".":
                    emb.add(i*big+k)
                else:
                    break
        elif A[i][j]=="^":
            emb.add(i*big+j)
            for k in reversed(range(i)):
                if A[k][j]==".":
                    emb.add(k*big+j)
                else:
                    break
        elif A[i][j]=="v":
            emb.add(i*big+j)
            for k in range(i+1,H):
                if A[k][j]==".":
                    emb.add(k*big+j)
                else:
                    break
for xy in emb:
    A[xy//big][xy%big]="#"
#(sy,sxからの距離を出力)
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
for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            si,sj = i,j
        elif A[i][j]=="G":
            gi,gj = i,j
A[gi][gj]="."
print(bfs(si,sj)[gi*W+gj])