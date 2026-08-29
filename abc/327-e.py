def main():
    N = int(input())
    P = list(map(int,input().split()))
    from math import sqrt
    dp = [[0 for j in range(N)] for k in range(N+1)]
    mother = 0
    ans = -10**9
    mother = 1
    debuff = 1200
    for j in range(N):
        dp[1][j] = P[j]
        temp = P[j]-debuff
        if temp>ans:
            ans = temp
    for k in range(2,N+1):
        mother *= 0.9
        mother += 1
        debuff = 1200/sqrt(k)
        ma = dp[k-1][k-2]
        for j in range(k-1,N):
            dp[k][j] = ma*0.9+P[j]
            if dp[k-1][j]>ma:
                ma = dp[k-1][j]
            temp = (dp[k][j]/mother)-debuff
            if temp>ans:
                ans = temp
    print(ans)
main()