N,M,K = map(int,input().split())
A = list(map(int,input().split()))
mod=998244353
A.sort()
free = A.count(0)
A = A[free:]
#とりあえず各値ごとに場合の数を求める
pascal = [[] for i in range(5000)]
pascal[0]= [1 for i in range(5000)]
for i in range(1,5000):
    for j in range(5000):
        if j==0:
            pascal[i].append(1)
            continue
        pascal[i].append((pascal[i-1][j]+pascal[i][j-1])%mod)
ans_sum = 0
for ak in range(1,M+1):
    ans = 0
    down  = K
    up = N-K+1
    for a in A:
        if a<=ak:
            down-=1
        if a>=ak:
            up-=1
    if up<0:
        up=0
    if down<0:
        down=0
    if free-up<0 or free-down<0:
        continue
    #print(ak,up,down,free)
    #ak以下がdown個以上、ak以上がup個以上
    #ak未満がfree-up以下
    #i=0について計算
    temp = 0
    for j in range(-down+free+1):
        temp+=pascal[free-j][j]*pow(M-ak,j,mod)%mod
        temp%=mod
    ans+=temp
    ans%=mod
    #print(ans)
    for i in range(1,free-up+1):
        if i>=down:
            ans+=pow(M-ak+1,free-i,mod)*pascal[i][free-i]%mod*pow(ak-1,i,mod)%mod
            ans%=mod
            continue
        temp+=pascal[free-down][down-i]*pow(M-ak,free-down+1,mod)%mod
        temp%=mod
        temp*=pow(M-ak+1,mod-2,mod)
        temp%=mod
        ans+=temp*pascal[i][free-i]%mod*pow(ak-1,i,mod)%mod
        ans%=mod
        #print(ans)
    ans_sum += ak*ans%mod
    ans_sum%=mod
mother = pow(M,free,mod)
ans_sum*=pow(mother,mod-2,mod)
ans_sum%=mod
print(ans_sum)