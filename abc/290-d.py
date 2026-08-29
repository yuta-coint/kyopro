T = int(input())
from math import gcd
for case in range(T):
    N,D,K = map(int,input().split())
    D%=N
    g = gcd(N,D)
    loop = N//g
    print((D*(K-1)+((K-1)//loop))%N)
