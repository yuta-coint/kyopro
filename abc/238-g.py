from math import sqrt, ceil
import sys
input = sys.stdin.readline
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    sqrt_n = ceil(sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    lip = []
    for i in range(n):
        if prime[i]:
            lip.append(i)            
    return lip
def factorization(numa):
    arr = []
    hp = numa
    for i in range(2, int(-(-numa**0.5//1))+1):
        while hp%i==0:
            hp //= i
            arr.append(i)
    if hp>1:
        arr.append(hp)
    return(arr)
primes = sieve_of_eratosthenes(10**6+1)
l_primes = len(primes)
d_primes = {primes[i]:i for i in range(l_primes)}
from random import randint
cnt = [0 for i in range(l_primes)]
h1 = [randint(1,1<<60) for i in range(l_primes)]
h2 = [randint(1,1<<60) for i in range(l_primes)]
h3 = [h1[i]^h2[i] for i in range(l_primes)]
N,Q = map(int,input().split())
A = list(map(int,input().split()))
check = []
for a in A:
    ha = 0
    for p in (factorization(a)):
        pn = d_primes[p]
        if cnt[pn]==0:
            ha^=h1[pn]
            cnt[pn]=1
        elif cnt[pn]==1:
            ha^=h2[pn]
            cnt[pn]=2
        else:
            ha^=h3[pn]
            cnt[pn]=0
    check.append(ha)
sum_ha = [0]
for i in range(N):
    sum_ha.append(sum_ha[-1]^check[i])
for _ in range(Q):
    L,R=  map(int,input().split())
    if sum_ha[L-1]==sum_ha[R]:
        print("Yes")
    else:
        print("No")
