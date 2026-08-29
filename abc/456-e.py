def TopologicalSort(G,N):
    rG = [set() for i in range(N)]
    for i in range(N):
        for j in G[i]:
            rG[j].add(i)
    inedge = [len(rG[i]) for i in range(N)]
    L = []
    import queue
    S = queue.Queue()
    for i in range(N):
        if inedge[i]==0:
            S.put(i)
    while not S.empty():
        n = S.get()
        L.append(n)
        for i in G[n]:
            inedge[i] -= 1
            if inedge[i] == 0:
                S.put(i)
    if N==len(L):
        return(L)
    else:
        return(-1)
T = int(input())
def solve():
    N, M = map(int,input().split())
    edges = [tuple(map(int,input().split())) for i in range(M)]
    W = int(input())
    G = [set() for _ in range(N * W)]
    S = [input() for i in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        for i in range(W):
            #片方でも平日があれば除外
            if S[u][i] == "o" and S[v][(i + 1)%W] == "o":
                G[N * i + u].add(N * ((i + 1)%W) + v)
            if S[v][i] == "o" and S[u][(i + 1)%W] == "o":
                G[N * i + v].add(N * ((i + 1)%W) + u)
    for u in range(N):
        for i in range(W):
            #片方でも平日があれば除外
            if S[u][i] == "o" and S[u][(i + 1)%W] == "o":
                G[N * i + u].add(N * ((i + 1)%W) + u)
    ans = TopologicalSort(G, N * W)
    if ans == -1:
        print("Yes")
    else:
        print("No")
for _ in range(T):
    solve()