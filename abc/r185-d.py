mod = 998244353
N,M = map(int,input().split())
#一回ガチャを回して戻ってくるのにかかる時間の期待値
#分母の行列式
half = 499122177
quot = half*half%mod
second = 3*half%mod*half%mod
mdet = [1,1]
sdet = [0,1]
#N=1で例外処理！
if M==1:
    gacha = 1
else:
    for i in range(2,M+1):
        mdet.append((mdet[i-1]-quot*mdet[i-2]%mod)%mod)
        sdet.append((mdet[i-1]+half*sdet[i-1]%mod)%mod)
    bunbo = (mdet[M-1]-half*mdet[M-2])%mod
    bunsi = (mdet[M-1]+sdet[M-1])%mod
    gacha = bunsi*pow(bunbo,mod-2,mod)%mod
#ガチャを回す回数の期待値
time = 0
for i in range(1,N+1):
    time += pow(i,mod-2,mod)
    time %= mod
time*=N
time%=mod
time = (2*time - 1)%mod
print(gacha*time%mod)