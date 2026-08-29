##########combination求めるときの前計算
mod = 998244353
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
###組み合わせをmodで割った余り（s+tCs、前計算だけ）
def combination_count(s,t):
    return(mothers[s]*mothers[t]%mod*powers[s+t]%mod)
N,K = map(int,input().split())
A = list(map(int,input().split()))
cnt = [0 for i in range(4*(10**5)+1)]
for i in range(N):
    cnt[A[i]]+=1
ans = 0
mex = []
temp = 0
for i in range(K+1):
    while cnt[temp]>0:
        temp+=1
    mex.append(temp)
    temp+=1
for i in range(K+1):
    if mex[i]==0:
        continue
    ans+=combination_count(mex[i]-1,K-i)
    ans%=mod
print(ans)