def main():
    n,P = map(int,input().split())
    dp = [[0 for i in range(6002)] for j in range(n+1)]
    dp[0][0]=1
    dp[1][2]=26
    for j in range(2,1+n):
        for i in range(2,3002):
            dp[j][i]+=dp[j-1][i-2]*25
            dp[j][i]%=P
            dp[j][i]+=dp[j-1][i]
            dp[j][i]%=P
            #この3つをいい感じに処理したい
            pow = [10,100,1000]
            for k in range(3):
                t = pow[k]
                if j>=t:
                    if i-k-2==0:
                        dp[j][i]-=dp[j-t][i-k-2]
                    if i-k-2>=0:
                        dp[j][i]-=dp[j-t][i-k-2]*25
                        dp[j][i]%=P
                    if i-k-3==0:
                        dp[j][i]+=dp[j-t][i-k-3]
                    if i-k-3>=0:
                        dp[j][i]+=dp[j-t][i-k-3]*25
                        dp[j][i]%=P
    ans = 0
    for i in range(n):
        ans+=dp[n][i]
        ans%=P
    print(ans)
main()
