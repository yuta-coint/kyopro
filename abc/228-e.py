n,k,m = map(int,input().split())
mod = 998244352
def bigpower(base,pow):
    num = 1
    i = len(bin(pow))-3
    while i>=0:
        num = num*num%mod
        if pow>>i & 1==1:
            num = num*base%mod
        i-=1
    return(num)
kn = bigpower(k%mod,n)
mod+=1
ans = bigpower(m,kn)
if m%mod==0:
    print(0)
else:
    print(ans)