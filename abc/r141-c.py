import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
P=list(map(lambda x:int(x)-1,input().split()))
Q=list(map(lambda x:int(x)-1,input().split()))
ans = [None for i in range(2*N)]
ok = True
ma = -1
mi = 2*N
for i in reversed(range(2*N)):
    if Q[i]<ma:
        ans[Q[i]]=1
    ma=max(Q[i],ma)
    mi=min(Q[i],mi)
mi = 2*N
ma = -1
for i in range(2*N):
    if Q[i]>mi:
        if ans[Q[i]]==1:
            ok = False
        ans[Q[i]]=-1
    ma=max(Q[i],ma)
    mi=min(Q[i],mi)
mi = 2*N
ma = -1
for i in range(2*N):
    if P[i]<ma:
        if ans[P[i]]==1:
            ok = False
        ans[P[i]]=-1
    ma=max(P[i],ma)
    mi=min(P[i],mi)
mi = 2*N
ma = -1
for i in reversed(range(2*N)):
    if P[i]>mi:
        if ans[P[i]]==-1:
            ok = False
        ans[P[i]]=1
    ma=max(P[i],ma)
    mi=min(P[i],mi)
#確定すべきところは確定したので最終確認
if None in ans or ok==False:
    print(-1)
else:
    cnt=0
    for i in range(2*N):
        cnt+=ans[P[i]]
        if cnt<0:
            ok=False
    if cnt!=0:
        ok=False
    cnt=0
    for i in range(N*2):
        cnt+=ans[Q[i]]
        if cnt<0:
            ok=False
    if cnt!=0:
        ok=False
    if ok:
        for i in range(2*N):
            if ans[i]==-1:
                ans[i]="("
            else:
                ans[i]=")"
        print(*ans,sep="")
    else:
        print(-1)


        



