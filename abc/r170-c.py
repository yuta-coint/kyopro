mod = 998244353
N,M = map(int,input().split())
S = list(map(int,input().split()))
if M>N:
    print(pow(M,N-sum(S),mod))
    exit()
cnt=M+1-sum(S)
#i種類登場するのは何通り？
dp = [0 for i in range(M+2)]
dp[0]=1
for i in range(N):
    if S[i]==0:
        #cnt種類以下に収める。
        for j in reversed(range(1,cnt+1)):
            dp[j] = (dp[j-1]*(M-j+1)%mod+dp[j]*j%mod)%mod
    else:
        cnt+=1
        for j in reversed(range(1,M+2)):
            dp[j] = dp[j-1]
    dp[0]=0
print(sum(dp)%mod)