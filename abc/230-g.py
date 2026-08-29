N = int(input())
P = [-1]+list(map(int,input().split()))
#メビウス関数を列挙する#########################
#素因数分解
def Moebius_calc(numa):
    hp = numa
    cnt_prime=1
    for i in range(2, int(-(-numa**0.5//1))+1):
        if hp%(i*i)==0:
            return(0)
        if hp%i==0:
            hp //= i
            cnt_prime *= -1
    if hp>1:
        cnt_prime *= -1
    return(cnt_prime)
Moebius = [0]+[Moebius_calc(i) for i in range(1,N+1)]
############################################
ans = 0
non_zero_mob = []
for i in range(2,N+1):
    if Moebius[i]!=0:
        non_zero_mob.append(i)
#print(non_zero_mob)
for i in non_zero_mob:
    #P[j]の列の中から
    temp = 0
    skipped = [P[j*i] for j in range((N+i)//i)]
    ls = len(skipped)
    for div in non_zero_mob:
        cnt = 0
        for j in range(ls):
            if skipped[j]%div==0:
                cnt+=1
        temp += (cnt*(cnt+1)//2)*Moebius[div]
    #print(i,temp)
    ans+=temp*Moebius[i]
print(ans)