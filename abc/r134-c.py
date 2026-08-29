mod = 998244353
###組み合わせをmodで割った余り（pCq、計算量q）
def bigpower(base,pow):
    num = 1
    for i in reversed(range(len(bin(pow)))):
        num = num*num%mod
        if pow>>i & 1:
            num = num*base%mod
        i+=1
    return(num)
def pcq(p,q):
    com = m
    for i in range(q):
        com *= p-i
        com %= mod
    return(com)
n,k  = map(int,input().split())
a = list(map(int,input().split()))
po = 1
for i in range(1,k):
    po*=i
    po%=mod
m = bigpower(po,mod-2)
rem = a[0]*2-k-sum(a)
if rem>=0:
    ans = pcq(rem+k-1,k-1)
    for i in range(1,n):
        ans*=pcq(a[i]+k-1,k-1)
        ans%=mod
    print(ans)
else:
    print(0)