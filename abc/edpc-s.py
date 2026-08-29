mod=10**9+7
K = list(input())
D = int(input())
for i in range(len(K)):
    K[i] = int(K[i])
#一桁少ないものからその10倍のもので答えを出せる。
dp = [0 for i in range(D)]
edge = 0
for i in range(len(K)):
    new_dp = [0 for amari in range(D)]
    for last_digit in range(10):
        for amari in range(D):
            new_dp[(amari+last_digit)%D]+=dp[amari]
            new_dp[(amari+last_digit)%D]%=mod
    for last_digit in range(K[i]):
        new_dp[(edge+last_digit)%D]+=1
        new_dp[(edge+last_digit)%D]%=mod
    edge+=K[i]
    edge%=D
    dp=new_dp
dp[edge]+=1
print((dp[0]-1)%mod)