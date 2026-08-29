#N問の解答状況256通り、所持金5000円
N,X = map(int,input().split())
probs = [tuple(map(int,input().split())) for i in range(N)]
dp = [[0 for i in range(1<<N)] for x in range(X+1)]
for x in range(X+1):
    for bits in range(1<<N):
        #各問題への提出を試みる。解答済みなら飛ばす。金欠でも飛ばす。
        for i in range(N):
            if (bits>>i)&1:
                continue
            if probs[i][1]>x:
                continue
            maru = dp[x-probs[i][1]][bits+(1<<i)]+probs[i][0]
            batu = dp[x-probs[i][1]][bits]
            kitai = maru*probs[i][2]+batu*(100-probs[i][2])
            kitai/=100
            if dp[x][bits]<kitai:
                dp[x][bits] = kitai
print(dp[-1][0])