H,W = map(int,input().split())
S = [list(input()) for i in range(H)]
l = H
r = 0
u = W
d = 0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            l = min(l,i)
            r = max(r,i)
            u = min(u,j)
            d = max(d,j)
ans = "Yes"
for i in range(l,r+1):
    for j in range(u,d+1):
        if S[i][j]==".":
            ans = "No"
print(ans)