N,M = map(int,input().split())
G = [[] for i in range(N)]
ans = -M
for i in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
for v in range(N):
    visited=[0 for i in range(N)]
    S = [v]
    ls = 1
    while ls>0:
        v = S.pop()
        ls-=1
        if visited[v]==1:
            continue
        visited[v]=1
        for i in G[v]:
            S.append(i)
            ls+=1
    ans+=sum(visited)-1
print(ans)