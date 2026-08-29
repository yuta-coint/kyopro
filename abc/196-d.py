#i行j列まで埋まっていて一畳をk個使っていて、境界がSであるものSは下に行くほど小さいビットにする
#縦向けと横向けに1畳を付け足すパターンと半畳を付け足すパターン
h,w,a,b = map(int,input().split())
dp = [[[0 for s in range(2**w)] for k in range(a+1)] for i in range(h*w-w+1)]
dp[0][0][0]=1
for k in range(a+1):
    for S in range(2**w):
        if k==0 and S==0:
            continue
        dp[0][k][S]+=dp[0][k][S>>1]
        if S&3==3 and k!=0:
            dp[0][k][S]+=dp[0][k-1][S>>2]
for i in range(1,h*w-w+1):
    for k in range(a+1):
        for S in range(2**w):
            if S&1==0:
                dp[i][k][S] = dp[i-1][k][(S>>1)+(1<<(w-1))]
                continue
            dp[i][k][S] = dp[i][k][S-1]
            if k == 0:
                continue
            dp[i][k][S] += dp[i-1][k-1][S>>1]
            if S&3==3 and (i-1)%w!=0:
                dp[i][k][S] += dp[i-2][k-1][(S>>2)+(3<<(w-2))]
print(dp[h*w-w][a][2**w-1])
#for i in range(h*w-w+1):
#    print(dp[i])