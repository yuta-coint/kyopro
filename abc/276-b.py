N,M = map(int,input().split())
G = [[] for i in range(N+1)]
for i in range(M):
    A,B = map(int,input().split())
    G[A].append(B)
    G[B].append(A)
for i in range(1,N+1):
    G[i].sort()
for i in range(1,N+1):
    ans = [len(G[i])]+G[i]
    print(*ans)