H,W = map(int,input().split())
a = [input() for i in range(H)]
ans = [[0 for j in range(W)] for i in range(H)]
mod = 10**9+7
ans[0][0]=1
for i in range(H):
    for j in range(W):
        if a[i][j]=="#":
            continue
        if i>0 and a[i-1][j]==".":
            ans[i][j]+=ans[i-1][j]
        if j>0 and a[i][j-1]==".":
            ans[i][j]+=ans[i][j-1]
        ans[i][j]%=mod
print(ans[H-1][W-1])