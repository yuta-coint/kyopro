N = int(input())
A = list(map(int,input().split()))
sA = [0]
for i in range(N):
    sA.append(sA[-1]+A[i])
mod = 10**9+7
dp = [[0 for j in range(N+1)] for i in range(N+1)]
#j個目までをi個に切り分ける
for j in range(1,N+1):
    dp[1][j]=1
for i in range(2,N+1):
    for j in range(i+1,N+1):
        if sA[]


