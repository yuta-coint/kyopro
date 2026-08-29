#何円以下まで全部買えるかを二分探索
#k番目が2k+1 P[i]円
N,M = map(int,input().split())
ng = M+1
ok = 0
P = list(map(int,input().split()))
from math import floor,sqrt
while ok+1<ng:
    m = (ok+ng)//2
    cost=0
    for t in range(N):
        #何個買えるか
        s= (m+P[t])//(2*P[t])
        cost+=s*s*P[t]
    if cost<=M:
        ok=m
    else:
        ng=m
#改めてok円以下の物を全て買ったうえで次のやつを優先度付きキューに入れる。
ans = 0
for t in range(N):
    s = (ok+P[t])//(2*P[t])
    M -= s*s*P[t]
    ans += s
    P[t] = (2*s+1)*P[t]
P.sort()
#ほとんど同率一位を捌く時間
for t in range(N):
    if M>=P[t]:
        M-=P[t]
        ans += 1
    else:
        break
print(ans)        