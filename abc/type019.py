n = int(input())
a = list(map(int,input().split()))
#幅2*i,スタートj
dp = [[0 for j in range(2*n+1)] for i in range(n+1)]
#iは差a[j]-a[i+j-1]
for i in range(1,n+1):
    for j in range(2*n-i*2+1):
        temp = abs(a[j]-a[2*i+j-1])+dp[i-1][j+1]
        for k in range(1,i):
            temp = min(temp,abs(a[j+2*k]-a[2*i+j-1])+dp[k][j]+dp[i-1-k][j+2*k+1])
        dp[i][j]=temp
print(dp[n][0])