import math
import sys
input = sys.stdin.readline
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Optional, List
T = TypeVar('T')

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    #primeは素数判定機
    list_of_prime =[]
    for i in range(n+1):
        if prime[i]:
            list_of_prime.append(i)
    return(list_of_prime)
############################################
N,P  = map(int,input().split())
primes = sieve_of_eratosthenes(P)
primes_a = primes[:9]
primes_b = primes[9:]
fore = [1]
back = [1]
for p in primes_a:
    new_fore = []
    for i in fore:
        k=-1
        while i*(p**(k+1))<=N:
            new_fore.append(i*(p**(k+1)))
            k+=1
    fore = new_fore
for p in primes_b:
    new_back = []
    for i in back:
        k=-1
        while i*(p**(k+1))<=N:
            new_back.append(i*(p**(k+1)))
            k+=1
    back = new_back
ans = 0
back.sort()
for i in fore:
    ans+=bisect_right(back,N//i)
print(ans)