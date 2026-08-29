n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
#a1が活きている
dp = [0]
dp1= [0]
dp2 = [a[0]]
dp3= [a[0]]
dp.append(b[0])
dp1.append(a[1])
dp2.append(a[0])
dp3.append(max(dp2[1]+a[2],b[1]+dp2[1]))
for i in range(1,n-1):
    dp.append(min(b[i]+dp[i],dp1[i]))
    dp1.append(min(dp[i]+a[i+1],dp1[i]+a[i+1]+b[i]))
    dp2.append(min(b[i]+dp2[i],dp3[i]))
    dp3.append(min(dp2[i]+a[i+1],dp3[i]+a[i+1]+b[i]))
a1 = dp2[n-1]
a2 = dp1[n-1]
a3 = dp[n-1]+b[n-1]
a4 = dp3[n-1]+b[n-1]
print(min(a1,a2,a3,a4))
#print(dp)
#print(dp2)