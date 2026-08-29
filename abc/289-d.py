N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
B = set(B)
X = int(input())
dp = [False for i in range(X+1)]
dp[0]=True
for i in range(1,X+1):
    for a in A:
        if i-a<0:
            continue
        if dp[i-a]:
            dp[i]=True
    if i in B:
        dp[i]=False
if dp[X]:
    print("Yes")
else:
    print("No")
    