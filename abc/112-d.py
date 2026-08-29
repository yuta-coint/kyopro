#約数列挙
import math
n,m = map(int,input().split())
yaku = []
for i in range(1,math.floor(m**(1/2))+1):
    if m%i==0:
        yaku+=[i,m//i]
ans = 0
for i in yaku:
    if i*n<=m:
        ans = max(ans,i)
print(ans)
