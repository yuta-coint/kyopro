N,X=map(int,input().split())
dp = [0 for i in range(X+1)]
dp[0]=1
for i in range(N):
    A,B = map(int,input().split())
    if A>X:
        continue
    for mai in range(B):
        for yen in reversed(range(A,X+1)):
            dp[yen]|=dp[yen-A]
if dp[X]==1:
    print("Yes")
else:
    print("No")
