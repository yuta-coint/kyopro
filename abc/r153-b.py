H,W = map(int,input().split())
A = [list(input()) for i in range(H)]
Q = int(input())
tate = 0
yoko = 0
HT = 0
for i in range(Q):
    a,b = map(int,input().split())
    if HT ==1:
        a = H-a
        b = W-b
    tate+=a
    tate%=H
    yoko+=b
    yoko%=W
    HT^=1
ans = [[0 for i in range(W)] for i in range(H)]
if HT==0:
    for i in range(H):
        for j in range(W):
            ans[i][j]=A[(i+tate)%H][(j+yoko)%W]
else:
    for i in range(H):
        for j in range(W):
            ans[H-1-i][W-1-j]=A[(i+tate)%H][(j+yoko)%W]
for i in range(H):
    print(*ans[i],sep="")