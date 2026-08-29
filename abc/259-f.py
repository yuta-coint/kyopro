def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')
    N = int(input())
    d  =list(map(int,input().split()))
    G = [[] for i in range(N)]
    First = [0 for i in range(N)]
    Second = [0 for i in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        u-=1
        v-=1
        G[u].append((w,v))
        G[v].append((w,u))
    unvisited = [True for i in range(N)]
    bro = [set() for i in range(N)]
    def dfs(v):
        unvisited[v]=False
        for w,i in G[v]:
            if unvisited[i]:
                bro[v].add((w,i))
                dfs(i)
        q = []
        temp=0
        for w,i in bro[v]:
            temp+=First[i]
            r = w-First[i]+Second[i]
            q.append(max(r,0))
        #print(q)
        q.sort(reverse=True)
        lb = len(bro[v])
        cnt =0
        cnt2=False
        if d[v]==0:
            cnt=0
            cnt2=False
        elif d[v]-1<lb:
            cnt=d[v]-1
            cnt2=True
        elif d[v]-1==lb:
            cnt = d[v]-1
        else:
            cnt=lb
        temp+=sum(q[:cnt])
        Second[v]=temp
        if cnt2:
            First[v]=temp+q[cnt]
        else:
            First[v]=temp
        if d[v]==0:
            Second[v]=-float('inf')
    dfs(0)
    #print(First)
    #print(Second)
    print(First[0])
main()