N,M = map(int,input().split())
G = [[] for i in range(N)]
ans = -M
for i in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
dim = [len(G[i]) for i in range(N)]
visited=[0 for i in range(N)]
def dfs(v):
    S = [v]
    edge = 0
    node = 0
    ls = 1
    while ls>0:
        v = S.pop()
        ls-=1
        if visited[v]==1:
            continue
        visited[v]=1
        node+=1
        edge+=dim[v]
        for i in G[v]:
            S.append(i)
            ls+=1
    if edge==node*2:
        return(False)
    else:
        return(True)
for i in range(N):
    if visited[i]==1:
        continue
    if dfs(i):
        print("No")
        break
else:
    print("Yes")
