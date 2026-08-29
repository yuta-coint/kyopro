N,M = map(int,input().split())
check=[[False for i in range(N)] for j in range(N)]
for _ in range(M):
    k = list(map(int,input().split()))
    for i in range(1,k[0]+1):
        for j in range(1,k[0]+1):
            check[k[i]-1][k[j]-1]=True
ans = "Yes"
for i in range(N):
    for j in range(N):
        if check[i][j]==False:
            ans="No"
print(ans)
