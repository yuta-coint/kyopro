import sys
input = sys.stdin.readline
n,m = map(int,input().split())
friend = [[False for i in range(n*2)] for j in range(n*2)]
mod = 998244353
#[i,j)での理想的な値
pattern = [[0 for i in range(n*2+1)] for i in range(n*2+1)]
for i in range(m):
    a,b = map(int,input().split())
    friend[a-1][b-1]=True
    friend[b-1][a-1]=True
for i in range(2*n-1):
    if friend[i][i+1]:
        pattern[i][i+2]=1
pas = [[0 for i in range(201)] for j in range(201)]
for i in range(201):
    pas[i][0]=1
    pas[0][i]=1
for i in range(1,201):
    for j in range(1,201):
        pas[i][j]=(pas[i][j-1]+pas[i-1][j])%mod
#print(pattern)
#[i,j)間での値を範囲が小さい順に評価していく
#左端の相手は誰ですか？どのタイミングで差し込みますか？
for r in range(4,2*n+2,2):
    r2 = r//2
    for i in range(2*n+1-r):
        j=i+r
        #一番左と二番目に左でペア
        if friend[i][i+1]:
            pattern[i][j]+=pattern[i+2][j]*r2%mod
            pattern[i][j]%=mod
        #一番左と一番右
        if friend[i][j-1]:
            pattern[i][j]+=pattern[i+1][j-1]
            pattern[i][j]%=mod
        for k in range(2,r-2,2):
            k2=k//2
            if friend[i][i+k+1]:
                pattern[i][j]+=pattern[i+1][i+k+1]*pattern[i+k+2][j]%mod*pas[k2+1][r2-k2-1]%mod
                pattern[i][j]%=mod
#print(pattern)
print(pattern[0][2*n])