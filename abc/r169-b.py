from bisect import bisect_left
N,S = map(int,input().split())
A = list(map(int,input().split()))
A_sum = [0]
for i in range(N):
    A_sum.append(A_sum[-1]+A[i])
ans = [0]
for i in range(1,N+1):
    k = bisect_left(A_sum,A_sum[i]-S)
    ans.append(ans[k]+i)
print(sum(ans))
    