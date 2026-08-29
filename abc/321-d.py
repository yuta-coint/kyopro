from bisect import bisect_left
N,M,P = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
#正規の値段で何回カウントされるかを調べればいい
ans = 0
for i in range(N):
    t = bisect_left(B,P-A[i])
    ans += t*A[i]
    ans += (M-t)*P
for i in range(M):
    ans += bisect_left(A,P-B[i])*B[i]
print(ans)