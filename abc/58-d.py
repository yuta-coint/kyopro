n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
mod = 10**9+7
x.sort()
y.sort()
ans1 =0
for i in range(n):
    ans1+=(2*i-n+1)*x[i]
    ans1%=mod
ans2 = 0
for i in range(m):
    ans2+=(2*i-m+1)*y[i]
    ans2%=mod
print((ans1*ans2)%mod)