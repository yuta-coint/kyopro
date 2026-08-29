N,M = map(int,input().split())
pair = [[0 for i in range(N+1)] for j in range(N+1)]
ans = (N*(N-1))//2
for _ in range(M):
    a = list(map(int,input().split()))
    for j in range(N-1):
        if pair[a[j]][a[j+1]]==0:
            ans-=1
            pair[a[j]][a[j+1]]=1
            pair[a[j+1]][a[j]]=1
print(ans)