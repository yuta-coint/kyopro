#https://noshi91.hatenablog.com/entry/2021/06/29/044225
import networkx as nx
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
B = []
for i in range(N):
    for j in range(N):
        B.append(A[i][j])
V = N*N
G = nx.DiGraph()
for i in range(V * 5 + 2):
    G.add_node(i)
s = V * 5
t = V * 5 + 1
alpha = 0
theta  = [[0 for j in range(6)] for i in range(V)]
phi = [[[[0 for l in range(6)] for k in range(6)] for j in range(V)] for i in range(V)]
for p1 in range(V-1):
    cand_p2 = []
    if p1%N < N-1:
        cand_p2.append(p1+1)
    if p1//N < N-1:
        cand_p2.append(p1+N)
    for p2 in cand_p2:
        if B[p1] != 0 and B[p2] != 0:
            alpha += (B[p1] - B[p2]) * (B[p1] - B[p2])
        if B[p1] != 0 and B[p2] == 0:
            for j in range(6):
                theta[p2][j] += (j - B[p1]) * (j - B[p1])
        if B[p1] == 0 and B[p2] != 0:
            for j in range(6):
                theta[p1][j] += (j - B[p2]) * (j - B[p2])
        if B[p1] != 0 and B[p2] != 0:
            for i in range(6):
                theta[p1][i] += i * i
                theta[p2][i] += i * i
            for i in range(5):
                for j in range(5):
                    G.add_edge(p1 * 5 + i,p2 * 5 + j,2)            
bottom = 0
for v in range(V):
    bottom += theta[v][5]
    for i in range(5):
        if theta[v][i+1]-theta[v][i] > 0:
            G.add_edge(s,v * 5 + i,theta[v][i+1]-theta[v][i])
        elif -theta[v][i+1]+theta[v][i] > 0:
            G.add_edge(v * 5 + i,t,-theta[v][i+1]+theta[v][i])
            bottom -= -theta[v][i+1]+theta[v][i]
INF = 10**9
#基本の無限の辺を張る作業
for v in range(V):
    for i in range(4):
        G.add_edge(v * 5 + i + 1,v * 5 + i,INF)
flow_value, flows = nx.maximum_flow(G, s, t)
print(flow_value + alpha + bottom)