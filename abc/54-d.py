import sys
input = sys.stdin.readline
n,ma,mb = map(int,input().split())
pl_mi = [[],[]]
just = []
for i in range(n):
    a,b,c = map(int,input().split())
    p = a*mb-b*ma
    if p>0:
        pl_mi[0].append([p,c])
    elif p==0:
        just.append(c)
    else:
        pl_mi[1].append([-p,c])
dp = [[float('inf') for _ in range(4000)] for j in range(2)]
for i in range(2):
    dp[i][0]=0
    for dif in pl_mi[i]:
        for j in reversed(range(dif[0],4000)):
            if dp[i][j-dif[0]]==float('inf'):
                continue
            dp[i][j]=min(dp[i][j],dif[1]+dp[i][j-dif[0]])
ans = 10**9
for i in range(1,4000):
    if dp[1][i]!=float('inf') and dp[0][i]!=float('inf'):
        ans = min(ans,dp[0][i]+dp[1][i])
if just!=[]:
    ans=min(ans,min(just))
if ans==10**9:
    print(-1)
else:
    print(ans)       
            