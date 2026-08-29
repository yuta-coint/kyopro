H,W = map(int,input().split())
c = [list(input()) for i in range(H)]
for i in range(H):
    for j in range(W):
        c[i][j] = ord(c[i][j])-ord("a")
#各行各列について、色の数をカウントする。
ot = [[0 for j in range(26)] for i in range(H)]
oy = [[0 for i in range(26)] for j in range(W)]
tt = [0 for i in range(H)]
ty = [0 for j in range(W)]
for i in range(H):
    for j in range(W):
        if ot[i][c[i][j]]==0:
            tt[i]+=1
        ot[i][c[i][j]]+=1
        if oy[j][c[i][j]]==0:
            ty[j]+=1
        oy[j][c[i][j]]+=1
##楯列と横列において一種類しかなさそうなら取り除く
from collections import deque
q = deque()
for i in range(H):
    if tt[i]==1:
        q.append(i)
for j in range(W):
    if ty[i]==1:
        q.append(-j-1)
#新しくttやtyが一になったらその列の文字を全部取り除く
while q:
    v = q.pop()
    if v>0:
        
    
