def main():
    import sys
    input = sys.stdin.readline
    N,M = map(int,input().split())
    G = [[] for i in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    ans = [i for i in range(N+1)]
    ans1 = [sum(G[i])+i for i in range(N+1)]
    G1 = [[i] for i in range(N+1)]
    for i in range(1,N+1):
        for v in G[i]:
            G1[i].append(v)
            for t in G[v]:
                G1[i].append(t)
    #print(G1)
    ans2 = [sum(set(G1[i])) for i in range(N+1)]
    G2 = [G1[i] for i in range(N+1)]
    for i in range(1,N+1):
        for v in G[i]:
            for s in G[v]:
                for t in G[s]:
                    G2[i].append(t)
    ans3 = [sum(set(G2[i])) for i in range(N+1)]
    Q = int(input())
    for i in range(Q):
        x,k = map(int,input().split())
        if k==0:
            print(ans[x])
        elif k==1:
            print(ans1[x])
        elif k==2:
            print(ans2[x])
        else:
            print(ans3[x])
main()