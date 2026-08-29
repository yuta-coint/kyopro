from math import gcd
import sys
import typing
input = sys.stdin.readline
 
class CSR:
    def __init__(
            self, n: int, edges: typing.List[typing.Tuple[int, int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)
 
        for e in edges:
            self.start[e[0] + 1] += 1
 
        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]
 
        counter = self.start.copy()
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1
 #Euler tourを作る#################################################
 
class SCCGraph:
    '''
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    '''
 
    def __init__(self, n: int) -> None:
        self._n = n
        self._edges: typing.List[typing.Tuple[int, int]] = []
 
    def num_vertices(self) -> int:
        return self._n
 
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self._edges.append((from_vertex, to_vertex))
 
    def scc_ids(self) -> typing.Tuple[int, typing.List[int]]:
        g = CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n
 
        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))
 
        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids
 
            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])
 
            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1
 
        for i in range(self._n):
            if order[i] == -1:
                dfs(i)
 
        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]
 
        return group_num, ids
 
    def scc(self) -> typing.List[typing.List[int]]:
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: typing.List[typing.List[int]] = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)
 
        return groups
def solve(N,M,edges):
    Gs = SCCGraph(N)
    for s,t in edges:
        Gs.add_edge(s,t)
    sccd_all = Gs.scc()
    check = -1
    for i in range(len(sccd_all)):
        if 0 in sccd_all[i]:
            check=i
            break
    sccd = sccd_all[check]
    if len(sccd)==1:
        print("No")
        return 0
    set_scced = set(sccd)
    #print(sccd)
    G = [[] for i in range(N)]
    for i in range(M):
        u,v = edges[i]
        if (not (u in set_scced)) or (not (v in set_scced)):
            continue
        G[u].append(v)
    S = []
    S.append((-1,0))
    depth = [10**9 for i in range(N)]
    cycle = []
    #無向グラフの場合と違って後退辺があったとしても、その直接の親に繋がるとは限らないのか
    while S:
        w,v = S.pop()
        if depth[v]!=10**9:
            continue
        if w!=-1:
            depth[v]=depth[w]+1
        else:
            depth[v]=0
        for i in G[v]:
            if depth[i]==10**9:
                S.append((v,i))
    for v in range(N):
        for i in G[v]:
            cycle.append(abs(depth[v]+1-depth[i]))
    #print(dist)
    #print(cycle)
    if len(cycle)==0:
        print("No")
        return 0
    g = cycle[0]
    for n in cycle:
        g  =gcd(n,g)
    while g%2==0:
        g//=2
    while g%5==0:
        g//=5
    if g==1:
        print("Yes")
    else:
        print("No")
T = int(input())
for case in range(T):
    N,M = map(int,input().split())
    e = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(M)]
    solve(N,M,e)