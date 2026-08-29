from math import gcd
a,b,c = map(int,input().split())
g = gcd(gcd(a,b),c)
print((a+b+c)//g-3)