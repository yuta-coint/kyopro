def twelvefold3(ball,box,mod):
    a = 0
    temp = 1
    for i in range(box):
        temp*=(box-i)
        temp*=pow(i+1,mod-2,mod)
        temp%=mod
        if (box-i)&1:
            a+=(temp*pow(i+1,ball,mod))%mod
        else:
            a-=(temp*pow(i+1,ball,mod))%mod
        a%=mod
    return a

def sterling2(ball,box,mod):
    b = twelvefold3(ball,box,mod)
    for i in range(box):
        b*=pow(i+1,mod-2,mod)
        b%=mod
    return b

N,K,P = map(int, input().split())
X_over_G  = [0 for i in range(K)]
X = [0 for i in range(K)]
n_fac = [1]
for i in range(1,50):
    n_fac.append(n_fac[-1]*i%P)
X_over_G.append(pow(2,K*(K-1)//2,P))
X.append(n_fac[K]*X_over_G[-1]%P)

for n in range(K+1,N+1):
    #とりあえずすべての頂点を区別した状態でスタートする。
    X.append(pow(2,n*(n-1)//2,P)*twelvefold3(n,K,P)%P)
    #バーンサイドの補題を用いる。S_{n}の軌道毎に数え上げを行い、過去の結果を使う。
    #あとはS_{n}について、k個の軌道を作る元が何個あるかを数え上げることになる。
    temp = 0
    for l in range(1,n):
        temp += n_fac[n-l]*sterling2(n,l,P)%P*X[l]%P
        temp%=P
    X_over_G.append(temp * pow(n_fac[n],-1,P) % P)
print(X)
print(X_over_G[-1])