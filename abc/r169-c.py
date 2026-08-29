#tで終わる数列の個数、iターン目にtが新たに始まった数、最後に潰された数
mod = 998244353
N = int(input())
A = list(map(int,input().split()))
#tで終わる数列の個数
dp = [0 for t in range(N+1)]
#iターン目に新たに立ったt
ad = [[0 for t in range(N+1)] for i in range(N)]
if A[0]==-1:
    for t in range(1,N+1):
        ad[0][t] = 1
        dp[t] = 1
else:
    dp[A[0]]=1
    ad[0][A[0]]=1
#tがつぶされた最終ターン
last_num = [-1 for i in range(N+1)]
for i in range(1,N):
    #print(dp)
    #print(ad)
    sdp = sum(dp)%mod
    new_dp = [0 for i in range(N+1)]
    if A[i]==-1:
        for t in range(1,N+1):
            ad[i][t] = sdp-dp[t]
            if last_num[t]<i-t:
                new_dp[t] = sdp-ad[i-t][t]
            else:
                new_dp[t] = sdp
    else:
        #A[i]でリセットする方法は
        t = A[i]
        new_dp[t] = sdp-dp[t]
        ad[i][t]= sdp-dp[t]
        #続ける方法
        for turn in range(max(last_num[t]+1,i-t+1),i):
            new_dp[t]+=ad[turn][t]
            new_dp[t] %= mod
        for num in range(1,N+1):
            if num!=t:
                last_num[num]=i
    for i in range(N+1):
        dp[i] = new_dp[i]
print(sum(dp)%mod)