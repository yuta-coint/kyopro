mod = 998244353
##########combination求めるときの前計算
powers = [1]
pw=1
for i in range(1,10**7+1):
    pw*=i
    pw%=mod
    powers.append(pw)
#iの階乗分の1
mothers = []
mother = powers[10**7]
mother = pow(mother,mod-2,mod)
for i in reversed(range(1,10**7+1)):
    mothers.append(mother)
    mother*=i
    mother%=mod
mothers.reverse()
mothers = [1]+mothers
##############################
###組み合わせをmodで割った余り（s+tCs、前計算だけ）
def combination_count(s,t):
    return(mothers[s]*mothers[t]%mod*powers[s+t]%mod)
N,M = map(int,input().split())
ans =0
#両端を3で割ったあまりが9通りある
for i in range(N):
    #とりあえず間の合計が(N-1+i)
    if M-(N-1+i)<0:
        break
    edge = combination_count(i,N-1-i)
    print(edge)
    if (M-(N-1+i))%3==0:
        temp = [0,1,1]
    elif (M-(N-1+i))%3==1:
        temp = [0,0,1]
    else:
        temp = [0,0,0]
    count_three = (M-(N-1+i))//3
    piece=0
    #print(count_three)
    for j in temp:
        if count_three-j<0:
            continue
        piece+=combination_count(count_three-j,N)
    ans+=piece*edge%mod
    ans%=mod
print(ans)