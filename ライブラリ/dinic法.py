# Dinic's algorithm
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
#グラフのエッジを取り込む
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
#sからtの最大流を求める
    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow
    #復元(カットされた結果、頂点がs側に残っているか判定)
    def restore(self,s):
        visited = [False for i in range(self.N)]
        q = deque([s])
        visited[s]=True
        while q:
            p = q.popleft()
            for e in self.G[p]:
                w, cap, rev = e
                if cap and not(visited[w]):
                    visited[w]=True
                    q.append(w)
        return(visited)
import sys
readline = sys.stdin.readline
write = sys.stdout.write

N,G,E = map(int, readline().split())
p = list(map(int, readline().split()))
#N:頂点の数
dinic = Dinic(N)
for i in range(E):
    a,b = map(int, readline().split())
    dinic.add_edge(a, b, 1)
    dinic.add_edge(b, a, 1)
for i in range(G):
    dinic.add_edge(p[i], N, 1)
write("%d\n" % dinic.flow(0, N))