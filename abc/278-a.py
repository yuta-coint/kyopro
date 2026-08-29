N,K = map(int,input().split())
A = list(map(int,input().split()))
if K>=N:
    ans = [0 for i in range(N)]
else:
    ans = A[K:] + [0 for i in range(K)]
print(*ans)