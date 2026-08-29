H,W = map(int,input().split())
C = [input() for i in range(H)]
ans = [0 for j in range(W)]
for i in range(H):
    for j in range(W):
        if C[i][j]=="#":
            ans[j]+=1
print(*ans)