def bigpower(base,pow):
    num = 1
    for i in reversed(range(len(bin(pow)))):
        num = num*num%mod
        if pow>>i & 1:
            num = num*base%mod
        i+=1
    return(num)
n = int(input())
mod = 10**9+7
factr = [1]
for i in range(1,n+1):
    factr.append(factr[-1]*i%mod)
for i in range(n):
    ans= 0
    for j in range(n):
        if n-j*i<j+1:
            break
        p = factr[n-j*i]*bigpower(factr[j+1],mod-2)%mod
        p*=bigpower(factr[n-j*i-j-1],mod-2)
        p%=mod
        ans+=p
        ans%=mod
    print(ans)