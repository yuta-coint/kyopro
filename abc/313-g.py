N = int(input())
a = list(map(int,input().split()))
a.sort()
fukuro = a[0]*N
for i in reversed(range(N)):
    a[i]-=a[0]
ans=a[-1]+1
mod  =998244353
#初項s,公差tの等差数列k項の和をNで割った商の和
def floor_sum(n,m,a,b):
    res = 0
    while True:
        if a >= m:
            res += (a//m)*n*(n-1)//2
            a %= m
        if b >= m:
            res += n*(b//m)
            b %= m
        if a*n+b < m:
            break
        u = (a*n+b)//m
        v = u*m-b
        res += (n-(v+a-1)//a)*u
        n,m,a,b = u,a,m,(a-v)%a
    return res
for i in range(1,N):
    #print(ans)
    ans+= floor_sum(a[i]-a[i-1],N,N-i,fukuro)
    ans %=mod
    fukuro+=(N-i)*(a[i]-a[i-1])
ans+=fukuro//N
ans%=mod
print(ans)