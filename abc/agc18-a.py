n,k = map(int,input().split())
a = list(map(int,input().split()))
from math import gcd
g = a[n-1]
for i in range(n-1):
    g = gcd(g,a[i])
if k%g==0 and k<=max(a):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")