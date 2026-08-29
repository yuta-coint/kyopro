N = int(input())
#センサー1の個数毎にセンサー2の個数の最小化を試みる。
INF = 10**24
D = list(map(int,input().split()))
L1,C1,K1 = map(int,input().split())
L2,C2,K2 = map(int,input().split())
dp = [0 for i in range(K1+1)]
for i in range(N):
    #センサー1を何個新たに使うか
    new = [INF for i in range(K1+1)]
    for c in range(K1+1):
        need = ((D[i]-c*L1-1)//L2)+1
        if need<0:
            need = 0
        for s in range(c,K1+1):
            if new[s]>dp[s-c]+need:
                new[s] = dp[s-c]+need
        if need == 0:
            break
    dp = new
ans = INF
for i in range(K1+1):
    if dp[i]>K2:
        continue
    if ans>dp[i]*C2+i*C1:
        ans = dp[i]*C2+i*C1
if ans==INF:
    print(-1)
else:
    print(ans)
