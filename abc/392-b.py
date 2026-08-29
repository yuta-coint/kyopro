N,M  = map(int,input().split())
ans = []
chk = [True for i in range(N+1)]
A = list(map(int,input().split()))
for i in range(M):
    chk[A[i]] = False
for i in range(1,N+1):
    if chk[i]:
        ans.append(i)
print(len(ans))
print(*ans)