N = int(input())
A = list(map(int,input().split()))
M = 25
S = [0 for i in range(M+1)]

for k in range(M):
    #2^kの倍数の総和
    d = {}
    cnt = {}
    for i in range(N):
        b = A[i]%(1<<k)
        if b in d:
            d[b] += A[i]
            cnt[b] += 1
        else:
            d[b] = A[i]
            cnt[b] = 1
        c = (-A[i])%(1<<k)
        if c in d:
            S[k] += d[c]
            S[k] += A[i] * cnt[c]
for k in range(M):
    S[k] -= S[k+1]
ans = 0
for k in range(M):
    ans += S[k]//(1<<k)
print(ans)