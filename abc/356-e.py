from sortedcontainers import SortedSet, SortedList, SortedDict
N = int(input())
A = list(map(int,input().split()))
A.sort()
S = SortedList(A)
ans = 0
for i in range(N):
    for j in range(1,100):
        l = S.bisect_left(A[i]*j)
        r = S.bisect_left(A[i]*(j+1))
        ans+=(r-l)*j
    for k in range(r,N):
        ans+=A[k]//A[i]
print(ans)