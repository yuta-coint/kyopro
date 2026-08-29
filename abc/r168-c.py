N,K = map(int,input().split())
S = input()
A = S.count("A")
B = S.count("B")
C = S.count("C")
mod = 998244353
##########combination求めるときの前計算
powers = [1]
pw=1
for i in range(1,10**6+1):
    pw*=i
    pw%=mod
    powers.append(pw)
#iの階乗分の1
mothers = []
mother = powers[10**6]
mother = pow(mother,mod-2,mod)
for i in reversed(range(1,10**6+1)):
    mothers.append(mother)
    mother*=i
    mother%=mod
mothers.reverse()
mothers = [1]+mothers
##############################
ans = 0
son = powers[A]*powers[B]%mod*powers[C]%mod
for i in range(K+1):
    if i>B:
        continue
    for j in range(K+1-i):
        if i+j>A:
            continue
        for l in range(K+1):
            if j+l>C:
                continue
            for k in range(K+1-l):
                if l+k>B or k>A:
                    continue
                m = i+j-k
                n = k+l-i
                if m<0 or n<0 or m+n>C:
                    continue
                if min(m,j)+min(k,i)+max(n,l)>K:
                    continue
                #ここまで確認すれば正当
                ans += son*mothers[m]%mod*mothers[n]%mod*mothers[k]%mod*mothers[l]%mod*mothers[i]%mod*mothers[j]%mod*mothers[C-m-n]%mod*mothers[B-k-l]%mod*mothers[A-i-j]%mod
                ans %= mod
print(ans)