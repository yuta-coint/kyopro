from atcoder.maxflow import MFGraph

from sys import stdout
N,A,B = map(int,input().split())
graph = MFGraph(N * N + 2)
A -= 1
B -= 1
now = (A,B)
for i in range(N):
    for j in range(N - 1):
        if (i + j) & 1:
            graph.add_edge(i * N + j, i * N + j + 1, 1)
            graph.add_edge(i + j * N, i + (j + 1) * N, 1)
        else:
            graph.add_edge(i * N + j + 1, i * N + j, 1)
            graph.add_edge(i + (j + 1) * N, i + j * N, 1)
for i in range(N):
    for j in range(N):
        if (i,j) == (A,B):
            continue
        if (i + j) & 1:
            graph.add_edge(N * N, i * N + j, 1)
        else:
            graph.add_edge(i * N + j, N * N + 1, 1)
graph.flow(N * N, N * N + 1)
if (A + B) & 1:
    graph.add_edge(N * N, A * N + B, 1)
else:
    graph.add_edge(A * N + B, N * N + 1, 1)
ans = graph.flow(N * N, N * N + 1)
aikata=  [0 for _ in range(N * N)]
for edge in graph.edges():
    u,v = edge.src, edge.dst
    if u >= N * N or v >= N * N:
        continue
    if edge.flow != 0:
        aikata[u] = v
        aikata[v] = u
if ans == 0:
    print("Second")
    stdout.flush()
    r,c = map(lambda x:int(x)-1,input().split())
    now = (r,c)
else:
    print("First")
    stdout.flush()
while now[0] >= 0:
    p = aikata[now[0] * N + now[1]]
    a,b = p // N, p % N
    print(a + 1, b + 1)
    stdout.flush()
    r,c = map(lambda x:int(x)-1,input().split())
    now = (r,c)
