N,K,X = map(int,input().split())
A = list(map(int,input().split()))
coupon = []
rem = []
ans = 0
for i in range(N):
    coupon.append(A[i]//X)
    rem.append(A[i]%X)
if sum(coupon)>=K:
    print(sum(A)-K*X)
else:
    K-=sum(coupon)
    rem.sort()
    if K>=N:
        print(0)
    else:
        print(sum(rem[:N-K]))

a,b = map(int,input().split())
leng = a**2+b**2
from math import sqrt
print(a/sqrt(leng),b/sqrt(leng))

lx = []
ly = []
for i in range(3):
    x,y = map(int,input().split())
    if x in lx:
        lx.remove(x)
    else:
        lx.append(x)
    if y in ly:
        lx.remove(y)
    else:
        lx.append(y)
print(x,y)