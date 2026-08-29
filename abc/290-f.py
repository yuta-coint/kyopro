T = int(input())
mod = 998244353
##########combination求めるときの前計算
powers = [1]
pw=1
for i in range(1,3*(10**6)+1):
    pw*=i
    pw%=mod
    powers.append(pw)
#iの階乗分の1
mothers = []
mother = powers[3*(10**6)]
mother = pow(mother,mod-2,mod)
for i in reversed(range(1,3*(10**6)+1)):
    mothers.append(mother)
    mother*=i
    mother%=mod
mothers.reverse()
mothers = [1]+mothers
##############################
###組み合わせをmodで割った余り（s+tCs、前計算だけ）
def combination_count(s,t):
    return(mothers[s]*mothers[t]%mod*powers[s+t]%mod)
for case in range(T):
    N = int(input())
    if N==2:
        print(1)
        continue
    ans = N*combination_count(N-3,N-1)%mod+combination_count(N-1,N-2)
    print(ans%mod)

