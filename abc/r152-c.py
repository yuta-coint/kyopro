N=int(input())
A = list(map(int,input().split()))
scale = A[1]-A[0]
from math import gcd
for i in range(N-1):
    scale = gcd(scale,A[i+1]-A[i])
scale*=2
print(A[N-1]-A[0]+min(A[0]%scale,A[N-1]%scale))