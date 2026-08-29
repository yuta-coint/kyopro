N = int(input())
A = list(map(int,input().split()))
ma = max(A)
ans = -1
for i in range(N):
    if ans<A[i]<ma:
        ans = A[i]
print(ans)