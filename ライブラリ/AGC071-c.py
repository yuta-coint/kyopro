from networkx import Graph,is_bipartite,biconnected_component_edges
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    g = Graph()
    cnt = [0 for i in range(N)]
    G = [[] for i in range(N)]
    for i in range(M):
        u,v = map(lambda x:int(x)-1,input().split())
        g.add_edge(u,v)
        cnt[u]+=1
        cnt[v]+=1
        G[u].append(v)
        G[v].append(u)
    if not (is_bipartite(g)):
        print("Yes")
        continue
    biconn_edge_components = list(biconnected_component_edges(g))
    #print(biconn_edge_components)
    L = len(biconn_edge_components)
    cnt = [{} for i in range(N)]
    for i in range(L):
        for s,t in biconn_edge_components[i]:
            if i in cnt[s]:
                cnt[s][i]+=1
            else:
                cnt[s][i]=1
            if i in cnt[t]:
                cnt[t][i]+=1
            else:
                cnt[t][i]=1

    ans = "No"
    for i in range(N):
        c_val = list(cnt[i].values())
        c_val.sort()
        temp = 1
        for c in c_val:
            if c>temp:
                ans = "Yes"
            temp+=c
    print(ans)