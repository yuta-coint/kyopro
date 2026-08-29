N = int(input())
A = list(map(int,input().split()))
A.sort()
sa = [A[i+1]-A[i] for i in range(N-1)]
g = sa[0]
from math import gcd
for i in range(1,N-1):
    g = gcd(g,sa[i])
if g==1:
    print(2)
else:
    print(1)