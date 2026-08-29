mod = 998244353
M,N = map(int,input().split())
X = list(map(int,input().split()))
#最初は全部選べる。
dp = [0 for i in range(1<<M)]
dp[-1]=1
op = [0 for i in range(M)]
for i in range(M):
    op[X[i]-1]+=1<<i
#mask = [(1<<M)-1-(1<<t) for t in range(M)]
for i in range(N):
    newdp = [0 for i in range(1<<M)]
    for choose in range(1<<M):
        for t in range(M):
            if (choose>>t)&1:
                p = choose-(1<<t)
                p|=op[t]
                newdp[p]+=dp[choose]
                newdp[p]%=mod
    dp = newdp
print(sum(dp)%mod)