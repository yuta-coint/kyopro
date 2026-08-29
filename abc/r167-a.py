N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(N-M):
    ans+=(A[i]+A[2*N-2*M-1-i])**2
for i in range(2*N-2*M,N):
    ans+=A[i]**2
print(ans)