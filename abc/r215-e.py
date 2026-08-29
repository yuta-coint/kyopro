T = int(input())
import sys
def solve():
    N= int(input())
    A= list(input())
    B= list(input())
    M = int(input())
    G = [set() for i in range(N)]
    rG = [set() for i in range(N)]
    labeled_G = [set() for i in range(N)]
    labeled_rG = [set() for i in range(N)]
    for i in range(M):
        u,v = map(int,input().split())
        u-=1
        v-=1
        G[u].add(v)
        rG[v].add(u)
        labeled_G[u].add((v,i))
        labeled_rG[v].add((u,i))
    reachable_from_A = [0 for i in range(N)]
    stk_A = []
    reachable_from_B = [0 for i in range(N)]
    stk_B = []
    r_reachable_from_A = [0 for i in range(N)]
    r_stk_A = []
    r_reachable_from_B = [0 for i in range(N)]
    r_stk_B = []
    iki = []
    kaeri = []
    for i in range(N):
        if A[i]=='1':
            reachable_from_A[i]=1
            r_reachable_from_A[i]=1
            stk_A.append(i)
            r_stk_A.append(i)
            iki.append(i)
        if B[i]=='1':
            reachable_from_B[i]=1
            r_reachable_from_B[i]=1
            stk_B.append(i)
            r_stk_B.append(i)
            kaeri.append(i)
    while stk_A:
        u = stk_A.pop()
        for v in G[u]:
            if reachable_from_A[v]==0:
                reachable_from_A[v]=1
                stk_A.append(v)
    while stk_B:
        u = stk_B.pop()
        for v in G[u]:
            if reachable_from_B[v]==0:
                reachable_from_B[v]=1
                stk_B.append(v)
    while r_stk_A:
        u = r_stk_A.pop()
        for v in rG[u]:
            if r_reachable_from_A[v]==0:
                r_reachable_from_A[v]=1
                r_stk_A.append(v)
    while r_stk_B:
        u = r_stk_B.pop()
        for v in rG[u]:
            if r_reachable_from_B[v]==0:
                r_reachable_from_B[v]=1
                r_stk_B.append(v)
    #デバッグ用に、r_reachableをエラー出力
    print(reachable_from_A,file=sys.stderr)
    print(reachable_from_B,file=sys.stderr)
    print(r_reachable_from_A,file=sys.stderr)
    print(r_reachable_from_B,file=sys.stderr)
    #Aに入っているものは全て、r_reachable_from_B
    for i in range(N):
        if A[i] == "1":
            if r_reachable_from_B[i] == 0 and B[i] == "0":
                print(-1)
                return 0
        else:
            if B[i] == "1" and reachable_from_A[i] == 0:
                print(-1)
                return 0
    #点をいくつか選んでXとする。AからAUXに行き、BからBUXに行けるようにできるか？
    return 0
for _ in range(T):
    solve()

    