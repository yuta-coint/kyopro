mod = 998244353
N,A,B,P,Q = map(int,input().split())
taka = [0 for i in range(N)]
#turnで高橋がゴールする場合の数
taka_step = []
taka[A]=1
matP = pow(P,mod-2,mod)
for turn in range(1,N-A+1):
    temp = 0
    for i in reversed(range(1,P+1)):
        if N-P-1+i<0:
            break
        temp+=i*taka[N-P-1+i]%mod
        temp%=mod
    #taka_step.append(temp)
    taka_step.append(temp*pow(matP,turn,mod)%mod)
    sum_taka = [0]
    for i in range(N):
        sum_taka.append((sum_taka[-1]+taka[i])%mod)
    for masu in range(N):
        if masu-P<0:
            taka[masu]=sum_taka[masu]
        else:
            taka[masu] = (sum_taka[masu]-sum_taka[masu-P])%mod
aoki = [0 for i in range(N)]
#turnで青木がゴールする場合の数
aoki_step = []
aoki[B]=1
matQ = pow(Q,mod-2,mod)
for turn in range(1,1+N-B):
    temp = 0
    for i in reversed(range(1,Q+1)):
        if N-Q-1+i<0:
            break
        temp+=i*aoki[N-Q-1+i]%mod
        temp%=mod
    #aoki_step.append(temp)
    aoki_step.append(temp*pow(matQ,turn,mod)%mod)
    sum_aoki = [0]
    for i in range(N):
        sum_aoki.append((sum_aoki[-1]+aoki[i])%mod)
    for masu in range(N):
        if masu-Q<0:
            aoki[masu]=sum_aoki[masu]
        else:
            aoki[masu] = (sum_aoki[masu]-sum_aoki[masu-Q])%mod
#print(taka_step)
#print(aoki_step)
ans = 0
taka_step_sum = [0]
for t in taka_step:
    taka_step_sum.append((taka_step_sum[-1]+t)%mod)
for i in range(len(aoki_step)):
    if i>=N-A:
        ans+=aoki_step[i]
    else:
        ans+=taka_step_sum[i+1]*aoki_step[i]%mod
    ans%=mod
print(ans)