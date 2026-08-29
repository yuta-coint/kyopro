N,S=map(int,input().split())
DP = [[-1 for i in range(S+1)] for i in range(N+1)]
tasche = [list(map(int,input().split())) for i in range(N)]
DP[0][0]=0
for i in range(1,N+1):
    a,b = tasche[i-1][0],tasche[i-1][1]
    for j in range(a,S+1):
        if DP[i-1][j-a]!=-1:
            DP[i][j]=0
    for j in range(b,S+1):
        if DP[i-1][j-b]!=-1:
            DP[i][j]=1
if DP[N][S]==-1:
    print('Impossible')
else:
    ans = []
    price = S
    for i in reversed(range(1,N+1)):
        if DP[i][price]==0:
            price-=tasche[i-1][0]
            ans.append("A")
        else:
            price-=tasche[i-1][1]
            ans.append("B")
    ans.reverse()
    print(*ans,sep="")