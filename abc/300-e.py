N=int(input())
#2,3,5の数を調べる
mod = 998244353
two = 0
three = 0
five = 0
while N%2==0:
    two+=1
    N//=2
while N%3==0:
    three+=1
    N//=3
while N%5==0:
    five+=1
    N//=5
if N>1:
    print(0)
    exit()
#1は存在価値がない
mother = pow(5,mod-2,mod)
dp =[[[0 for k in range(five+1)] for j in range(three+1)] for i in range(two+1)]
for i in range(two+1):
    for j in range(three+1):
        for k in range(five+1):
            if i==j==k==0:
                dp[i][j][k]=1
                continue
            if i>=1:
                dp[i][j][k]+=dp[i-1][j][k]
                dp[i][j][k]%=mod
            if i>=2:
                dp[i][j][k]+=dp[i-2][j][k]
                dp[i][j][k]%=mod
            if j>=1:
                dp[i][j][k]+=dp[i][j-1][k]
                dp[i][j][k]%=mod
            if k>=1:
                dp[i][j][k]+=dp[i][j][k-1]
                dp[i][j][k]%=mod
            if i>=1 and j>=1:
                dp[i][j][k]+=dp[i-1][j-1][k]
                dp[i][j][k]%=mod
            dp[i][j][k]*=mother
            dp[i][j][k]%=mod
print(dp[two][three][five])
            
    