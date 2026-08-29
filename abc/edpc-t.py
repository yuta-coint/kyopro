#それまでで何番目に小さいかでdp
N= int(input())
s = input()
dp = [1]
mod = 10**9+7
for i in range(1,N):
    if s[i-1]=="<":
        new_dp = [0]
        for t in range(i):
            new_dp.append((new_dp[-1]+dp[t])%mod)
    else:
        new_dp = [sum(dp)]
        for t in range(i):
            new_dp.append((new_dp[-1]-dp[t])%mod)
    dp = new_dp
print(sum(dp)%mod)