def main():
    import sys
    input = sys.stdin.readline
    import queue
    T=int(input())
    INF=10**9
    for _ in range(T):
        N,M = map(int,input().split())
        G = [[] for i in range(N)]
        con = [[False for i in range(N)] for j in range(N)]
        edges = []
        for i in range(M):
            u,v,w = map(int,input().split())
            G[u-1].append(v-1)
            G[v-1].append(u-1)
            edges.append((w,u-1,v-1))
            con[u-1][v-1]=True
            con[v-1][u-1]=True
        dist = []
        for j in range(N):
            visited = [False for i in range(N)]
            temp = [float('inf') for i in range(N)]
            q = queue.Queue()
            visited[j]=True
            q.put((j,0))
            while not q.empty():
                v = q.get()
                temp[v[0]]=v[1]
                for i in G[v[0]]:
                    if visited[i]==False:
                        visited[i]=True
                        q.put((i,v[1]+1))
            dist.append(temp)
        ans = float('inf')
        for i in edges:
            c,a,b=i[0],i[1],i[2]
            t = (dist[0][a]+1+dist[b][N-1])*c
            if t<ans:
                ans=t
            t = (dist[0][b]+1+dist[a][N-1])*c
            if t<ans:
                ans=t
            t = (dist[0][b]+1+dist[b][N-1])*c
            if t<ans:
                ans=t
            t = (dist[0][a]+1+dist[a][N-1])*c
            if t<ans:
                ans=t
        print(ans)
main()