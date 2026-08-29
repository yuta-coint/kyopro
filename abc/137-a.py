from math import gcd
L,R  =map(int,input().split())
l,r = L,R
ans = R-L
while True:
    if gcd(l,r)==1:
        break
    ans -= 1
    r-=1
for i in range(R-L-ans+1):
    l = L+i
    r = R
    temp = r-l
    for j in range(R-L-ans+1):
        if gcd(l,r)==1:
            break
        temp -= 1
        r-=1
    ans = max(ans,temp)
print(ans)



