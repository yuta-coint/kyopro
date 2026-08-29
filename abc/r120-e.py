N=int(input())
A = list(map(int,input().split()))
ok = 10**10
ng = 0
dist = [(A[i + 1] - A[i])//2 for i in range(N-1)]
#Pをでかく、Qを小さくする貪欲
while ng + 1 < ok:
    m = (ok + ng)//2
    #和がm
    P1 = m
    Q1 = 0
    #QがD[i-1]
    P2 = m
    Q2 = 0
    chk = True
    for i in range(1,N):
        d = dist[i-1]
        mQ = min(Q1,Q2)
        mP = max(P1,P2)
        P1,Q1 = m - mQ - d,mQ + d
        P2,Q2 = mP - d, d
        if P1 < 0:
            P1 = -10**24
            Q1 = 10**24
        if P2 < 0:
            P2 = -10**24
            Q2 = 10**24
    if P1 < 0 and P2 < 0:
        chk = False
    if chk:
        ok = m
    else:
        ng = m
print(ok)