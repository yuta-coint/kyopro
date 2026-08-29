def main():
    import sys
    input = sys.stdin.readline
    N,M = map(int,input().split())
    from heapq import heapify,heappop,heappush
    A = list(map(int,input().split()))
    G = [[] for i in range(N)]
    costs = [0 for i in range(N)]
    for i in range(M):
        u,v = map(lambda x:int(x)-1,input().split())
        G[u].append(v)
        G[v].append(u)
        costs[u]+=A[v]
        costs[v]+=A[u]
    q = [(costs[i],i) for i in range(N)]
    #print(q)
    done = [False for i in range(N)]
    heapify(q)
    ans = 0
    cnt = N
    while cnt>0:
        t,s = heappop(q)
        #print((t,s))
        #print(cnt)
        cnt-=1
        if done[s]:
            continue
        done[s]=True
        ans = max(ans,t)
        for i in G[s]:
            if done[i]:
                continue
            costs[i]-=A[s]
            heappush(q,(costs[i],i))
            cnt+=1
    print(ans)
main()