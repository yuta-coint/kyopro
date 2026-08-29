N = int(input())
points = [tuple(map(int,input().split())) for i in range(N)]
dp = [[float("inf") for j in range(N)] for i in range(N)]
def dist(p,q):
    return(((points[p][0]-points[q][0])**2+(points[p][1]-points[q][1])**2)**(1/2))
dp[0][0]=0
for j in range(1,N):
    dp[0][j]=dp[0][j-1]+dist(j-1,j)
for i in range(1,N):
    for j in range(N):
        if i>j:
            dp[i][j]=dp[j][i]
        elif i==j:
            continue
        else:
            if i+1<j:
                dp[i][j]=dp[i][j-1]+dist(j-1,j)
            else:
                for k in range(i):
                    if dp[i][j]>dp[k][i]+dist(k,j):
                        dp[i][j]=dp[k][i]+dist(k,j)
print(dp[N-2][N-1]+dist(N-2,N-1))