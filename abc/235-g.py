mod =998244353
##########combination求めるときの前計算
powers = [1]
pw=1
for i in range(1,5*10**6+1):
    pw*=i
    pw%=mod
    powers.append(pw)
#iの階乗分の1
mothers = []
mother = powers[5*10**6]
mother = pow(mother,mod-2,mod)
for i in reversed(range(1,5*10**6+1)):
    mothers.append(mother)
    mother*=i
    mother%=mod
mothers.reverse()
mothers = [1]+mothers
##############################
###組み合わせをmodで割った余り（s+tCs、前計算だけ）
def combination_count(s,t):
    return(mothers[s]*mothers[t]%mod*powers[s+t]%mod)
pow2 = [1]
for i in range(5*10**6):
    pow2.append(pow2[-1]*2%mod)
N,A,B,C = map(int,input().split())
#n個以上の庭が空集合になるような場合の数
n_empty = []
pat_a = 0
pat_b = 0
pat_c = 0
for i in range(A+1):
    pat_a+=combination_count(N-i,i)
    if pat_a>=mod:
        pat_a-=mod
    pat_a%=mod
for i in range(B+1):
    pat_b+=combination_count(N-i,i)
    if pat_b>=mod:
        pat_b-=mod
for i in range(C+1):
    pat_c+=combination_count(N-i,i)
    if pat_c>=mod:
        pat_c-=mod
n_empty.append(pat_a*pat_b%mod*pat_c%mod)
half = pow(2,mod-2,mod)
for gardens in reversed(range(N)):
    #庭の数が足りていない場合
    if A>=gardens:
        pat_a = pow2[gardens]
    else:
        pat_a+=combination_count(A,gardens-A)
        if pat_a>=mod:
            pat_a-=mod
        pat_a*=half
        pat_a%=mod
    if B>=gardens:
        pat_b = pow2[gardens]
    else:
        pat_b+=combination_count(B,gardens-B)
        if pat_b>=mod:
            pat_b-=mod
        pat_b*=half
        pat_b%=mod
    if C>=gardens:
        pat_c = pow2[gardens]
    else:
        pat_c+=combination_count(C,gardens-C)
        if pat_c>=mod:
            pat_c-=mod
        pat_c*=half
        pat_c%=mod
    n_empty.append(pat_a*pat_b%mod*pat_c%mod)
#print(n_empty)
#包除原理
ans = 0
for i in range(N+1):
    if i&1:
        ans-=n_empty[i]*combination_count(N-i,i)%mod
        if ans<0:
            ans+=mod
    else:
        ans+=n_empty[i]*combination_count(N-i,i)%mod
        if ans>=mod:
            ans-=mod
print(ans)
