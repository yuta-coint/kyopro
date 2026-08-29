mod = 998244353
N,M = map(int,input().split())
fac = [1]
for i in range(1,N+M+1):
    fac.append(fac[-1]*i%mod)
R = list(map(int,input().split()))
B = list(map(int,input().split()))
red= [0 for i in range(N)]
blue = [0 for i in range(N)]
for i in range(M):
    red[R[i]-1]+=1
    blue[B[i]-1]+=1
dp = [0 for i in range(1<<N)]
ans = 0
#嘘包除をしていた…
mot = [1]
for i in range(1,N+1):
    mot.append(pow(i,mod-2,mod))
pc = []
prs = []
for bits in range(1<<N):
    r_sum = 0
    b_sum = 0
    pop = 0
    for i in range(N):
        if (bits>>i)&1:
            r_sum+=red[i]
            b_sum+=blue[i]
            pop+=1
    pc.append(pop)
    if r_sum==b_sum:
        prs.append(r_sum)
        temp = fac[r_sum]*pop%mod
        temp %= mod
        sss = []
        u = bits
        while u:
            sss.append(u)
            u = (u-1)&bits
        for ss in sss:
            if ss==bits:
                continue
            if prs[ss]==-1:
                continue
            temp -= pc[ss]*dp[ss]%mod*fac[prs[bits-ss]]%mod
            temp %= mod
        dp[bits]=temp*mot[pop]%mod
        ans += temp*mot[pop]%mod*fac[M-r_sum]%mod
        ans %= mod
    else:
        prs.append(-1)
#fac[M-r_sum]*fac[r_sum]%mod*pop%mod
#print(dp)
print(ans*pow(fac[M],mod-2,mod)%mod)