a,b,c,d,e,f = map(int,input().split())
a*=100
b*=100
water = []
sugar = []
for i in range(f//a+1):
    for j in range(f//b+1):
        if a*i+b*j>f:
            break
        water.append(a*i+b*j)
msug = f*e//(100+e)
for i in range(msug//c+1):
    for j in range(msug//d+1):
        if c*i+d*j>msug:
            break
        sugar.append(c*i+d*j)
sugar.sort()
from bisect import bisect_right
m = 0
ans = (0,0)
for i in water:
    if i ==0:
        continue
    lsug = min((i*e)//100,f-i)
    if sugar[0]>lsug:
        continue
    s = sugar[bisect_right(sugar,lsug)-1]
    ratio = s/i
    if ratio>=m:
        ans = (i+s,s)
        m = ratio
print(*ans)