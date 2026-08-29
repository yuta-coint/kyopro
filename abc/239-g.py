# Dinic's algorithm復元付き
from collections import deque
from difflib import restore
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
        #追加でフローを流す
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
sys.setrecursionlimit(10**6)
write = sys.stdout.write

n,E = map(int, readline().split())
#N:頂点の数
N = 2*n+1
dinic = Dinic(N)
for i in range(E):
    a,b = map(int, readline().split())
    dinic.add_edge(a+n, b, float("inf"))
    dinic.add_edge(b+n, a, float('inf'))
c = list(map(int, readline().split()))
for i in range(2,n):
    dinic.add_edge(i, n+i, c[i-1])
print(dinic.flow(n+1, n))
vd = dinic.restore(n+1)
ans = []
for i in range(2,n):
    if vd[i]^vd[i+n]:
        ans.append(i)
print(len(ans))
print(*ans)
