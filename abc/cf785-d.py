t = int(input())
mod = 10**9+7
from math import gcd
for _ in range(t):
    b,q,y = map(int,input().split())
    c,r,z = map(int,input().split())
    if r%q!=0:
        print(0)
    elif (c-b)%q!=0:
        print(0)
    elif b>c or b+(y-1)*q<c+(z-1)*r:
        print(0)
    elif b>c-r or b+(y-1)*q<c+(z-1)*r+r:
        print(-1)
    else:
        #rの約数列挙してp候補探すぜ！
        ans = 0
        for i in range(1,10**5):
            if i*i>r:
                break
            if r%i==0:
                if gcd(i,q)*r==i*q:
                    ans+=(r//i)*(r//i)%mod
                    ans%=mod
            if i*i==r:
                break
            j=r//i
            if r%j==0:
                if gcd(j,q)*r==j*q:
                    ans+=(r//j)*(r//j)%mod
                    ans%=mod
        print(ans)