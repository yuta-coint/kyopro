N = int(input())
A = list(map(int,input().split()))
#なもりグラフのサイクルの中に入っているか問題
ans = [0 for i in range(N)]
visited = [-1 for i in range(N)]
ans = 0
for i in range(N):
    if visited[i]>=0:
        continue
    temp = i
    loop = []
    while visited[temp]==-1:
        loop.append(temp)
        visited[temp]=i
        temp = A[temp]-1
    if visited[temp]==i:
        ans+=len(loop)-loop.index(temp)
print(ans)