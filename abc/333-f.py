mod = 998244353
#1/2
half = pow(2,-1,mod)
N = int(input())
ans = [1]
for p in range(2,N+1):
    zero = [1]
    const = [0]
    for i in range(1,p):
        zero.append(zero[-1]*half%mod)
        const.append((const[-1]*half%mod+ans[i-1]*half%mod)%mod)
    ans = []
    #print(zero,const)
    z = const[-1]*pow(2-zero[-1],-1,mod)
    for i in range(p):
        ans.append((z*zero[i]%mod+const[i])%mod)
print(*ans)