H,W = map(int,input().split())
S = [input() for i in range(H)]
u,d,l,r = 0,10**9,10**9,0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            u = max(u,i)
            d = min(d,i)
            l = min(l,j)
            r = max(r,j)
for i in range(d,u+1):
    for j in range(l,r+1):
        if S[i][j]==".":
            print(i+1,j+1)
            exit()