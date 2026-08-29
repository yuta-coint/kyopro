import sys
input = sys.stdin.readline
#小さい方を大きい方に入れていく。それとは別に各々の箱のありかを管理する。
N,Q = map(int,input().split())
C = list(map(lambda x:int(x)-1,input().split()))
C = [set([C[i]]) for i in range(N)]
#C[i]の大きさ
sz = [1 for i in range(N)]
loca = [i for i in range(N)]
for i in range(Q):
    a,b = map(lambda x:int(x)-1,input().split())
    if sz[loca[a]]<sz[loca[b]]:
        p,q = loca[a],loca[b]
        emp = a
    else:
        p,q = loca[b],loca[a]
        emp = b
        loca[a],loca[b] = loca[b],loca[a]
    for ball in C[p]:
        if not(ball in C[q]):
            sz[q]+=1
        C[q].add(ball)
    C[p]=set()
    sz[p]=0
    print(sz[q])