import sys
input = sys.stdin.readline
#合計価値iを実現するための最大の容量
n,W = map(int,input().split())
dp = [float('inf') for i in range(100*n+1)]
dp[0]=0
for i in range(n):
    v,w = map(int,input().split())
    for j in reversed(range(v,100*n+1)):
        dp[j]=min(dp[j],dp[j-v]+w)
for ans in reversed(range(100*n+1)):
    if dp[ans]<=W:
        print(ans)
        break
