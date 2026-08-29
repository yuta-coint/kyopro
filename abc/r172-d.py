N= int(input())
ans = [[N**2 for i in range(N)] for j in range(N)]
for i in range(N):
    ans[i][i]=10**8
for i in reversed(range(1,N*(N-1)//2+1)):
    a,b = map(int,input().split())
    a-=1
    b-=1
    ans[a][b]+=i
    ans[b][a]+=i
for i in range(N):
    print(*ans[i])
dist = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            dist[i][j]+=(ans[i][k]-ans[j][k])**2

for i in range(N):
    print(*dist[i])