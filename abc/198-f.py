#バーンサイドの補題を用いる。
#立方体の回転群は以下の成分からなる。全部足して24で割る。
S = int(input())
S -= 6
mod = 998244353
ans = 0
#自明元…一つ。s+5C5通り。
ans = (S+5)*(S+4)%mod*(S+3)%mod*(S+2)%mod*(S+1)%mod*pow(120,-1,mod)%mod
#軸をfixして半回転…3つ。a+a+b+b+c+d = Sを数える。
if S&1:
    T = S//2
    cnt = ((T+2)**3 - (T+2))%mod
else:
    T = S//2
    cnt = (((T+2)**3 - (T+2))//2)%mod
    cnt += (((T+1)**3 - (T+1))//2)%mod
    cnt %= mod
ans += cnt
ans %= mod
#軸をfixして1/4回転…6つ。a+a+a+a+c+d = Sを数える。
#(S+1)+(S-3)
temp = (S+1)//4
amari = (S+1)%4
ans += ((amari + S+1)*(temp+1)*3)%mod
ans %= mod
#対角線を軸に120度回転…8つ。a+a+a+b+b+b = Sを数える。
if S%3 == 0:
    ans += ((S//3)+1)*8%mod
    ans %= mod
#辺同士を結ぶ軸の場合…6つa+a+b+b+c+c = Sを数える。
if S%2 == 0:
    T = S//2
    ans += ((T+2)*(T+1)*3)%mod
    ans %= mod
print(ans)
ans *= pow(24,-1,mod)
ans %= mod
print(ans)