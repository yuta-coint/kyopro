N,M = map(int,input().split())
ans = 0
G = [set() for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    u-=1
    v-=1
    if u==v:
        ans+=1
        continue
    if v in G[u]:
        ans+=1
        continue
    G[u].add(v)
    G[v].add(u)
print(ans)