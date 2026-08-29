H,W = map(int,input().split())
N = min(H,W)
ans = [0 for i in range(N+1)]
C = [["." for i in range(W+2)]]
for i in range(H):
    C.append(["."]+list(input())+["."])
C.append(["." for i in range(W+2)])
for i in range(1,H+1):
    for j in range(1,W+1):
        if C[i][j]=="#" and C[i-1][j-1]=="#" and C[i-1][j+1]=="#" and C[i+1][j-1]=="#" and C[i+1][j+1]=="#":
            n=0
            while C[i+n][j+n]=="#":
                n+=1
            ans[n-1]+=1
print(*ans[1:])
            