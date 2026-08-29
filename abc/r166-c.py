mod = 998244353
fibo = [1,1]
for i in range(2*(10**6)+5):
    fibo.append((fibo[i]+fibo[i+1])%mod)
fibo_sum = [1]
for i in range(1,10**6+2):
    fibo_sum.append((fibo_sum[-1]*fibo[2*i])%mod)
T = int(input())
for case in range(T):
    H,W = map(int,input().split())
    if H>W:
        H,W = W,H
    print(fibo_sum[H]*fibo_sum[H]%mod*pow(fibo[2*H+1],W-H,mod)%mod)