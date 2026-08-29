N,M = map(int,input().split())
interrval = []
inl = [[] for i in range(N+1)]
inr = [[] for i in range(N+1)]
dp = [[0 for r in range(N+1)] for l in range(N+1)]
for i in range(M):
    l,r = map(int,input().split())
    interrval.append((l-1,r))
    inl[l-1].append(r)
    inr[r].append(l-1)
for i in range(N+1):
    inl[i].sort()
    inr[i].sort(reverse=True)
interrval.sort()
INF = 10**9
for width in range(1,N+1):
    for l in range(1,N+1-width):
        r = l+width
        ma = r
        dp[l][r]=dp[l][r-1]
        cnt = 0
        for li in inr[r]:
            if li<l:
                break
            cnt+=1
            if dp[l][ma-1]+cnt>dp[l][r]:
                dp[l][r]=dp[l][ma-1]+cnt
            ma = li
        cnt = 0
        mi = l
        if dp[l][r]<dp[l+1][r]:
            dp[l][r] = dp[l+1][r]
        for ri in inl[l]:
            if ri>r:
                break
            cnt+=1
            if dp[mi+1][r]+cnt>dp[l][r]:
                dp[l][r] = dp[mi+1][r]+cnt
            mi = ri
print(dp[0][N])