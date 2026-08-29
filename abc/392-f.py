import bisect
N,Q = map(int,input().split())
A = list(map(int,input().split()))
LIS = [-1]
ans = [-1 for _ in range(Q)]
chk = [[] for i in range(N)]
for j in range(Q):
    R,X = map(int,input().split())
    chk[R-1].append((j,X))
for i in range(N):
    a = A[i]
    if a > LIS[-1]:
        LIS.append(a)
    else:
        LIS[bisect.bisect_left(LIS, a)] = a
    for j,x in chk[i]:
        ans[j] = bisect.bisect_right(LIS, x)-1
        
for i in range(Q):
    print(ans[i])