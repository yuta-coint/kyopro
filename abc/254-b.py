N = int(input())
ans = [[0 for j in range(i+1)] for i in range(N)]
for i in range(N):
    ans[i][i]=1
    ans[i][0]=1
for i in range(1,N):
    for j in range(1,i):
        ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
for i in range(N):
    print(*ans[i])