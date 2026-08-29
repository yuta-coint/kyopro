N = int(input())
mod = 10**9+7
ans = 1
for i in range(N):
    A = list(map(int,input().split()))
    ans*=sum(A)
    ans%=mod
print(ans)
    