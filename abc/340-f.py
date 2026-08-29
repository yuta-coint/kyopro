#ax+by=gcd(a,b) の整数解 (x,y) ただし、絶対値の和を最小化
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
X,Y = map(int,input().split())
from math import gcd
#両方正だとおもってあとで符号はガチャガチャやる
sgnx = 1
if X<0:
    sgnx = -1
    X=-X
sgny = 1
if Y<0:
    sgny = -1
    Y = -Y
if gcd(X,Y)>2:
    print(-1)
    exit()
elif gcd(X,Y)==2:
    a,b = EEA(Y,X)
    b*=-1
else:
    a,b = EEA(Y,X)
    a*=2
    b*=-2
if sgnx==-1:
    b*=-1
if sgny==-1:
    a*=-1
print(a,b)
    