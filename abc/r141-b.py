import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
mod =998244353
candidate = []
keta = len(bin(M))-2
pow2 = 1
for i in range(keta-1):
    candidate.append(pow2)
    pow2*=2
    pow2%=mod
candidate.append(M-pow2+1)
#print(candidate)
if keta<N:
    print(0)
else:
    dp = [0 for i in range(N+1)]
    dp[0]=1
    for i in range(keta):
        for j in reversed(range(1,N+1)):
            dp[j]+=dp[j-1]*candidate[i]%mod
            dp[j]%=mod
        #print(dp)
    print(dp[N])
