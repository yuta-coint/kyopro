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
N,A,B,C,X = map(int,input().split())
#とりあえず、ext_euc(a,b)を(x,y)としておく。
x,y = EEA(A,B)
from math import gcd,ceil
g = gcd(A,B)
#kを動かしていく。gcdみてアウトっぽいなら、continueして、セーフっぽいなら答えが初期解が一つ出てくるので数える。つらい。
ans = 0
for k in range(1,N+1):
    if (X-C*k)%g>0:
        continue
    #とりあえず答えを一つ求める。
    x1,y1 = x*((X-C*k)//g),y*((X-C*k)//g)
    #幅はa,bではみ出さないことを考える。
    #1<=x1+sa<=Nなるsの範囲と1<=y1-tb<=Nなるtの範囲を調べればいい。
    a = B//g
    b = A//g
    #print(x1,y1,a,b)
    s_min = 1+(1-x1-1)//a
    s_max = (N-x1)//a
    t_min = 1+(y1-N-1)//b
    t_max = (y1-1)//b
    ans+=max(0,min(t_max,s_max)-max(t_min,s_min)+1)
    #print(ans)
print(ans)