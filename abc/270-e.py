N,K = map(int,input().split())
A = list(map(int,input().split()))
#リンゴをk個食べる上で最小のターン数を二分探索で考える
ok = 0
ng = 10**18
while ok+1<ng:
    mid = (ok+ng)//2
    eat = 0
    for i in range(N):
        chance = mid//N
        if i>=mid%N:
            if A[i]>=chance:
                eat+=chance
            else:
                eat+=A[i]
        else:
            if A[i]>=chance+1:
                eat+=chance+1
            else:
                eat+=A[i]
    if eat<=K:
        ok=mid
    else:
        ng=mid
ans = []
for i in range(N):
    chance = ok//N
    if i>=ok%N:
        if A[i]>=chance:
            ans.append(A[i]-chance)
        else:
            ans.append(0)
    else:
        if A[i]>=chance+1:
            ans.append(A[i]-chance-1)
        else:
            ans.append(0)
print(*ans)