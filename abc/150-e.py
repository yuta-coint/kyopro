n = int(input())
c = list(map(int,input().split()))
c.sort(reverse=True)
mod = 10**9+7
ans = 0
for i in range(n):
    ans += c[i]*(i+2)
    ans%=mod
for i in range(2*n-2):
    ans*=2
    ans%=mod
print(ans)
