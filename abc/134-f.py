from copy import copy
n,K = map(int,input().split())
mod = 10**9+7
dp = [[[1]]]
if K&1:
    print(0)
    exit()
for i in range(1,n+1):
    dpi = []
    for j in range(i+1):
        dpij = []
        for k in range(i*i+i+1):
            temp = 0
            if j-2>=0 and 0<=k-2*i<=i*(i-1):
                temp+=((i-j+1)**2)*dp[i-1][j-2][k-2*i]
                temp%=mod
            if j-1>=0 and 0<=k-i<=i*(i-1):
                temp+=(2*i-2*j+1)*dp[i-1][j-1][k-i]
                temp%=mod
            if j<=i-1 and k<=i*(i-1):
                temp+=dp[i-1][j][k]
                temp%=mod
            dpij.append(temp)
        dpi.append(dpij)
    dp.append(copy(dpi))
print(dp[n][n][(K+n*n+n)>>1])
