import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
def main():
    n = int(input())
    G = [[] for i in range(n)]
    for i in range(n-1):
        a,b = map(lambda x:int(x)-1,input().split())
        G[a].append(b)
        G[b].append(a)
    logn = len(bin(n))-1
    #iの2**j個先の親を求める。何もない場合は-1を出力する
    mother = [[-1 for i in range(n+1)] for j in range(logn)]
    depth = [-1 for i in range(n)]
    ord = [0 for i in range(n)]
    d = 0
    cnt = 0
    stack = [0]
    depth[0]=0
    while stack:
        v = stack.pop()
        ord[v] = cnt
        cnt+=1
        for i in G[v]:
            if depth[i]==-1:
                depth[i] = depth[v]+1
                mother[0][i]=v
                stack.append(i)
    for i in range(1,logn):
        for j in range(n):
            mother[i][j]=mother[i-1][mother[i-1][j]]
    #print(mother)
    def LCA(u,v):
        if depth[u]>depth[v]:
            u,v = v,u
        gap = depth[v]-depth[u]
        f = 0
        while gap>0:
            if gap&1:
                v = mother[f][v]
            gap>>=1
            f+=1
        for i in reversed(range(logn)):
            if mother[i][u]!=mother[i][v]:
                u = mother[i][u]
                v = mother[i][v]
        if u == v:
            return(u)
        else:
            return(mother[0][u])
    #print(depth)
    Q = int(input())
    for _ in range(Q):
        kv = list(map(lambda x:int(x)-1,input().split()))
        kv[0]+=1
        if kv[0]==2:
            l = LCA(kv[1],kv[2])
            print(depth[kv[1]]+depth[kv[2]]-depth[l]*2)
        elif kv[0]==3:
            a,b,c = kv[1],kv[2],kv[3]
            la = LCA(b,c)
            lb = LCA(c,a)
            lc = LCA(a,b)
            #print(a,b,c,la,lb,lc)
            print(depth[a]+depth[b]+depth[c]-depth[la]-depth[lb]-depth[lc])
        else:
            ki = []
            for i in range(1,kv[0]+1):
                ki.append((ord[kv[i]],kv[i]))
            ki.sort()
            ans = 0
            for i in range(kv[0]-1):
                ans+=depth[ki[i][1]]
                ans-=depth[LCA(ki[i][1],ki[i+1][1])]
            ans-=depth[LCA(ki[kv[0]-1][1],ki[0][1])]
            ans+=depth[ki[kv[0]-1][1]]
            print(ans)
main()
        