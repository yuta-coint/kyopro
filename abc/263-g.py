def main():
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
    import math
    import sys
    input = sys.stdin.readline
    def sieve_of_eratosthenes(n):
        prime = [True for i in range(n+1)]
        prime[0] = False
        prime[1] = False

        sqrt_n = math.ceil(math.sqrt(n))
        for i in range(2, sqrt_n):
            if prime[i]:
                for j in range(2*i, n+1, i):
                    prime[j] = False
        #primeは素数判定機
        list_of_prime =[]
        for i in range(n+1):
            if prime[i]:
                list_of_prime.append(i)
        return(list_of_prime)
    prime_check = set(sieve_of_eratosthenes(10**4))
    def pc(n):
        if n in prime_check:
            return(True)
        elif n<=10**4:
            return(False)
        else:
            for i in prime_check:
                if n%i==0:
                    return(False)
            else:
                return(True)
    N = int(input())
    #N:頂点の数
    dinic = Dinic(2*N+2)
    num = []
    for i in range(N):
        a,b = map(int, input().split())
        num.append((a,b))
    for i in range(N):
        dinic.add_edge(0,i+1,num[i][1])
        #print(0,i+1,num[i][1])
        dinic.add_edge(i+N+1,2*N+1,num[i][1])                
        #print(i+N+1,2*N+1,num[i][1])
        for j in range(N):
            if pc(num[i][0]+num[j][0]):
                dinic.add_edge(i+1,j+N+1,float('inf'))
                #print(i+1,j+N+1,float('inf'))
    print(dinic.flow(0, 2*N+1)//2)
main()