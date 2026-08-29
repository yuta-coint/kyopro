import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
P = [-1]+list(map(lambda x:int(x)-1,input().split()))
child_count = [0 for i in range(N)]
for i in range(1,N):
    child_count[P[i]]+=1
for i in range(Q):
    Mv = list(map(lambda x:int(x)-1,input().split()))
    setv = set(Mv[1:])
    ans = 0
    for v in setv:
        ans+=child_count[v]
        if P[v] in setv:
            ans-=1
        else:
            ans+=1
        #print(i,v,ans)
    print(ans)

