N,M = map(int,input().split())
A = list(map(int,input().split()))
cnt = [0 for i in range(M)]
for i in range(N):
    X = list(map(int,input().split()))
    for j in range(M):
        cnt[j]+=X[j]
ans = "Yes"
for i in range(M):
    if A[i]>cnt[i]:
        ans = "No"
print(ans)