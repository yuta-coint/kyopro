# (10**18)*a/b <= p <= (10**18)*c/d を満たす a,b,c,d <= n を求める
def stern_brocot(p, n):
    la = 0; lb = 1
    ra = 1; rb = 0
    lu = ru = 1
    lx = 0; ly = 1
    rx = 1; ry = 0
    while lu or ru:
        ma = la + ra; mb = lb + rb
        if p * mb < ma*(10**18):
            ra = ma; rb = mb
            if ma <= n and mb <= n:
                rx = ma; ry = mb
            else:
                lu = 0
        else:
            la = ma; lb = mb
            if ma <= n and mb <= n:
                lx = ma; ly = mb
            else:
                ru = 0
    # lx/ly <= √p <= rx/ry
    return lx, ly, rx, ry
c = input()
r=0
for i in range(len(c)):
    if i>=2:
        r+=int(c[i])*(10**(19-i))
N = int(input())
Lx,Ly,Rx,Ry = stern_brocot(r,N)
if Lx == Rx and Ly==Ry:
    print(Lx,Ly)
else:
    gosa1 = Ly*Ry*r-Ry*Lx*(10**18)
    gosa2 = Rx*Ly*(10**18)-Ly*Ry*r
    if gosa1<=gosa2:
        print(Lx,Ly)
    else:
        print(Rx,Ry)

from fractions import Fraction
r = input()
N= int(input())
r = Fraction(r)-Fraction(10**(-50))
ans = Fraction(r).limit_denominator(N)
print(ans.numerator,ans.denominator)