N,a,b,c = map(int,input().split())
A = list(map(int,input().split()))
from math import gcd
ab = a*b//(gcd(a,b))
bc = c*b//(gcd(c,b))
ac = a*c//(gcd(a,c))
abc = bc*a//(gcd(a,bc))
L = [1,a,b,ab,c,ac,bc,abc]
dp = [10**24 for i in range(8)]
dp[0]=0
for i in range(N):
    new = [10**24 for i in range(8)]
    for bits in range(8):
        if A[i]%L[bits]==0:
            cost=0
        else:
            cost=L[bits]-(A[i]%L[bits])
        #print(cost)
        for old in range(8):
            if new[old|bits]>dp[old]+cost:
                new[old|bits]=dp[old]+cost
    dp = new
    #print(dp)
print(dp[7])
