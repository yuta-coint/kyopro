#ax+by=gcd(a,b) の整数解 (x,y) ただし、絶対値の和を最小化
#両方正じゃないと動かない
def EEA(a,b):
    if a == 0:
        return(0,1)
    elif b == 0:
        return(1,0)
    elif a>=b:
        r = a//b
        p,q = EEA(a%b,b)
        return(p,q-r*p)
    else:
        r = b//a
        p,q = EEA(a,b%a)
        return(p-r*q,q)
from math import gcd
#不定ほうていしきをpythonで解けばいい
mod = 998244353
N,A,B,C = map(int,input().split())
G = gcd(B,C)
ans1 = 0
ans2 = 0
frac= [1,1]
for i in range(1,10**6):
    frac.append(i*frac[-1]%mod)
for x in range(3*(10**5) + 1):
    if x * A > N:
        break
    Y = N - x * A
    if Y%G != 0:
        continue
    S = Y //G
    y,z = EEA(B,C)
    y *= S
    z *= S
    t = C//G
    s = B//G
    mi = max(y//t,(-z)//s)
    ma = min((-y)//t,z//s)
    ans1 += max(0,ma-mi+1)
    L  = B*C//G
    start = Y*B%L
    
    
    