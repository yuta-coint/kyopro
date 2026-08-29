import sys
input = sys.stdin.readline
def main():
    N,M = map(int,input().split())
    G = [[] for i in range(N+1)]
    for i in range(M):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    import queue
    S = queue.LifoQueue()
    S.put(1)
    unvisited = [True for i in range(N+1)]
    unvisited[1]=False
    while not S.empty():
        v = S.get()
        if v!=1:
            print(v)
            v = v[1]
        for i in G[v]:
            if unvisited[i]:
                unvisited[i]=False
                S.put((i,v))
    S = queue.Queue()
    S.put(1)
    unvisited = [True for i in range(N+1)]
    unvisited[1]=False
    while not S.empty():
        v = S.get()
        for i in G[v]:
            if unvisited[i]:
                unvisited[i]=False
                print(v,i)
                S.put(i)
main()