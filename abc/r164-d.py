mod = 998244353
N = int(input())
T = input()
plus = T.count("+")
minus = T.count("-")
d1=N-plus
d2=N-minus
pascal = [[0 for i in range(d2+1)] for j in range(d1+1)]
for i in range(d1+1):
    for j in range(d2+1):
        if i==0 or j==0:
            pascal[i][j]=1
        else:
            pascal[i][j]=(pascal[i-1][j]+pascal[i][j-1])%mod
qes = 0
elec = 0
ans = 0
for i in range(2*N):
    if T[i]=="+":
        for pl in range(qes+1):
            mi=qes-pl
            if mi<0 or mi>d2 or pl>d1:
                continue
            k = abs(2*(elec+pl-mi)+1)
            ans+=pascal[pl][mi]*pascal[d1-pl][d2-mi]%mod*k%mod
            ans%=mod
        elec+=1
    elif T[i]=="-":
        elec-=1
    else:
        #プラスが入った場合を数えておく
        for pl in range(qes+1):
            mi=qes-pl
            if mi<0 or mi>d2 or pl+1>d1:
                continue
            k = abs(2*(elec+pl-mi)+1)
            ans+=pascal[pl][mi]*pascal[d1-pl-1][d2-mi]%mod*k%mod
            ans%=mod
        qes+=1
print(ans)