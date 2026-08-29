from networkx import Graph,is_bipartite
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    g = Graph()
    cnt = [0 for i in range(N)]
    G = [[] for i in range(N)]
    for i in range(M):
        u,v = map(int,input().split())
        g.add_edge(u-1,v-1)
        cnt[u-1]+=1
        cnt[v-1]+=1
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    if not (is_bipartite(g)):
        print("Yes")
        continue
    amari = cnt
    chk = [True for i in range(N)]
    for i in range(N):
        if amari[i]==1:
            t = i
            while amari[t]==1:
                amari[t]-=1
                chk[t] = False
                for j in G[t]:
                    if chk[j]:
                        amari[j]-=1
                        if amari[j]==0:
                            chk[j] = False
                        t = j
                        break
    ans = "No"
    for i in range(N):
        if amari[i]>cnt[i]-amari[i]+1:
            ans = "Yes"
    print(ans)