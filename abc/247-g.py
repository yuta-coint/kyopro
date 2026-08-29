from heapq import *
import sys
input = sys.stdin.readline
 
sys.setrecursionlimit(10 ** 9)
 

def main():
    class MinCostFlow:
        INF = 10**18
    
        def __init__(self, N):
            self.N = N
            self.G = [[] for i in range(N)]
    
        def add_edge(self, fr, to, cap, cost):
            forward = [to, cap, cost, None]
            backward = forward[3] = [fr, 0, -cost, forward]
            self.G[fr].append(forward)
            self.G[to].append(backward)
    
        def flow(self, s, t, f):
            N = self.N
            G = self.G
            INF = MinCostFlow.INF
    
            res = 0
            H = [0]*N
            prv_v = [0]*N
            prv_e = [None]*N
    
            d0 = [INF]*N
            dist = [INF]*N
    
            while f:
                dist[:] = d0
                dist[s] = 0
                que = [(0, s)]
    
                while que:
                    c, v = heappop(que)
                    if dist[v] < c:
                        continue
                    r0 = dist[v] + H[v]
                    for e in G[v]:
                        w, cap, cost, _ = e
                        if cap > 0 and r0 + cost - H[w] < dist[w]:
                            dist[w] = r = r0 + cost - H[w]
                            prv_v[w] = v
                            prv_e[w] = e
                            heappush(que, (r, w))
                if dist[t] == INF:
                    return None
    
                for i in range(N):
                    H[i] += dist[i]
    
                d = f
                v = t
                while v != s:
                    d = min(d, prv_e[v][1])
                    v = prv_v[v]
                f -= d
                res += d * H[t]
                v = t
                while v != s:
                    e = prv_e[v]
                    e[1] -= d
                    e[3][1] += d
                    v = prv_v[v]
            return res
    big = 1<<40
    N = int(input())
    ##座標圧縮
    men=[list(map(int,input().split())) for i in range(N)]
    sa = [men[i][0] for i in range(N)]
    sb = [men[i][1] for i in range(N)]
    sc = [men[i][2] for i in range(N)]
    ta = sorted(set(sa))
    tb = sorted(set(sb))
    da = {v:i+1 for i, v in enumerate(ta)}
    db = {v:i+1 for i, v in enumerate(tb)}
    sa = list(map(lambda v:da[v],sa))
    sb = list(map(lambda v:db[v],sb))
    #終わり
    n = max(max(sa),max(sb))
    ans = []
    Gr = MinCostFlow(2*n+2)
    for i in range(N):
        Gr.add_edge(sa[i],sb[i]+n,1,big-sc[i])
    for i in range(1,n+1):
        Gr.add_edge(0,i,1,0)
        Gr.add_edge(n+i,2*n+1,1,0)
    for i in range(1,n+1):
        #flow使うと保存されるから「追加で」一つづつ処理していく感じになるのか
        rf = Gr.flow(0,2*n+1,1)
        if rf is None:
            break
        ans.append(big-rf)
        if i!=1:
            ans[i-1]+=ans[i-2]
    print(len(ans))
    for i in ans:
        print(i)
main()