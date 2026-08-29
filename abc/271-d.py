N,S = map(int,input().split())
sa = []
base = 0
for i in range(N):
    a,b = map(int,input().split())
    base+=a
    sa.append(b-a)
dp = [[-1 for i in range((10**4)+1)] for i in range(N+1)]
dp[0][base]=0
for i in range(1,N+1):
    for j in range(10**4+1):
        if dp[i-1][j]!=-1:
            dp[i][j]=0
            continue
        if 0<=j-sa[i-1]<10**4+1:
            if dp[i-1][j-sa[i-1]]!=-1:
                dp[i][j]=1
if dp[N][S]==-1:
    print("No")
else:
    print("Yes")
    ans=[0 for i in range(N+1)]
    for i in reversed(range(1,N+1)):
        if dp[i][S]==0:
            ans[i]="H"
        else:
            ans[i]="T"
            S-=sa[i-1]
    print(*ans[1:],sep="")