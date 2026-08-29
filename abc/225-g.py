import sys
input = sys.stdin.readline
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
def main():
    H, W, C=  map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    if W == 1:
        ans = 0
        for i in range(H):
            if A[i][0] > 2 * C:
                ans += A[i][0] - 2 * C
        print(ans)
        exit()
    dinic = Dinic(H*W + 2)
    s = H * W
    g = H * W + 1
    base = 0
    for i in range(H):
        for j in range(W):
            base += A[i][j]
            cost = 0
            if i == H - 1:
                cost = C * 2
            elif j == 0 or j == W - 1:
                cost = C
            dinic.add_edge(s, i * W + j, cost)
            dinic.add_edge(i * W + j, g, A[i][j])
            if i != H - 1 and j != 0:
                dinic.add_edge((i + 1) * W + (j - 1), i * W + j, C)
            if i != H - 1 and j != W - 1:
                dinic.add_edge((i + 1) * W + (j + 1), i * W + j, C)
    ans = dinic.flow(s, g)
    print(base - ans)
main()