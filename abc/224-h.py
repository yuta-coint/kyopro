import networkx as nx
L, R = map(int,input().split())
G = nx.DiGraph()
G.add_nodes_from(range(L + R + 2))
A = list(map(int,input().split()))
for i in range(1, L + 1):
    G.add_edge(0, i, weight = 0, capacity = A[i - 1])
B = list(map(int,input().split()))
for i in range(L + 1, L + R + 1):
    G.add_edge(i, L + R + 1, weight = 0, capacity = B[i - L - 1])
max_flow = min(sum(A),sum(B))
C = [list(map(int,input().split())) for i in range(L)]
for i in range(L):
    for j in range(R):
        G.add_edge(i + 1, L + j + 1, weight = 100 - C[i][j], capacity = max_flow)
mincostFlow = nx.max_flow_min_cost(G, 0, L + R + 1)
mincost = nx.cost_of_flow(G, mincostFlow)
print(100*(max_flow) - mincost)
