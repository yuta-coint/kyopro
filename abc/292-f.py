A,B = map(int,input().split())
from math import sqrt,acos,degrees
if A<B:
    A,B = B,A
if A>B*sqrt(3):
    print(2*B/sqrt(3))
    exit()
ok = max(A,B)
ng = min(2*B/sqrt(3),2*A/sqrt(3))
while ng-ok>10**(-11):
    m=(ng+ok)/2
    if degrees(acos(B/m)+acos(A/m))<30:
        ok=m
    else:
        ng=m
print(ok)