N,C = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
dp = []
S = sum(A)
A[C-1]+=1
key = A[C-1]
A.sort(reverse=True)
for i in range(N):
    if A[i] == key:
        pin = i
ans = []
A_sum = -1
seki_sum = S
for i in range(N):
    A_sum += A[i]
    ans.append(seki_sum*pow(A_sum,-1,mod)%mod)
    seki_sum += A[i]*ans[i]%mod
    seki_sum %= mod
print(ans[pin])