N = int(input())
norma = 0
ks = []
for i in range(N):
    x,y,z = map(int,input().split())
    norma+=z
    if x>y:
        ks.append((0,z))
    else:
        ks.append(((y-x+1)//2,z))
norma=(norma+1)//2
dp = [10**24 for i in range(norma+1)]
dp[0]=0
for cost,pay in ks:
    #i議席以上を取得するために必要な鞍替え人数
    if pay>norma:
        pay = norma
    for i in reversed(range(pay,norma+1)):
        if dp[i-pay]+cost<dp[i]:
            dp[i]=dp[i-pay]+cost
    for i in reversed(range(norma)):
        if dp[i+1]<dp[i]:
            dp[i]=dp[i+1]
print(dp[i])