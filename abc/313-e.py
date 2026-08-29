N = int(input())
S = list(input())
for i in range(N):
    S[i]=int(S[i])
for i in range(N-1):
    if S[i]>=2 and S[i+1]>=2:
        print(-1)
        exit()
mod = 998244353
ans = 0
for i in reversed(range(1,N)):
    ans+=(1+(S[i]-1)*(ans+1))%mod
    ans%=mod
print(ans)
